from datetime import datetime as dt
from math import ceil
from variable_constants import activities, act, act1
from constants import *

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.patches import Patch
offset = 0


def bar_chart(steps):
    global offset
    save_activities = set([i[0] for i in steps])

    # dict of times
    activities_times = {}
    for activity_name in ACTIVITIES:
        if activity_name in save_activities:
            activities_times |= {activity_name: []}

    for i, activity in enumerate(steps):
        pivot = steps[i + 1][1] if i < len(steps) - 1 else dt.now().timestamp()
        activities_times[activity[0]].append(pivot - activity[1])
    AVERAGE_DAY = {}
    for activity_name in ACTIVITIES:
        if activity_name == "Void" or activity_name not in save_activities:
            continue
        AVERAGE_DAY |= {activity_name: 0}
    START_DAY = dt.fromtimestamp(steps[0][1]).weekday()
    EXPERIMENT_START_TIME = steps[0][1]
    ALL_EXPERIMENT_TIME = sum([sum(activities_times[i]) for i in activities_times])

    fig, axs = plt.subplot_mosaic(
        (["main"], ["average"]),
        figsize=(PLOT_WIDTH, PLOT_START_HEIGTH + ALL_EXPERIMENT_TIME // (
                24 * h) * PLOT_HEIGTH_STEP if FULL else PLOT_START_HEIGTH + 14 * PLOT_HEIGTH_STEP),
        gridspec_kw={
            "height_ratios": [
                (ALL_EXPERIMENT_TIME // (24 * h) + 2 if ALL_EXPERIMENT_TIME >= 48 * h else 2) if FULL else 14,
                1]}
    )

    fig.canvas.manager.set_window_title("Распределение времени")
    if EXCLUDE_VOIDS and "Void" in ACTIVITIES:
        ALL_EXPERIMENT_TIME -= sum(activities_times["Void"])

    # print hours and percentages
    print(f"Всего: {round(ALL_EXPERIMENT_TIME / h, 1)}ч\n")
    for activity in activities_times:
        if activity == "Void":
            continue

        AVERAGE_DAY[activity] = sum(activities_times[activity])
        print(f"""{activity}: {round(AVERAGE_DAY[activity] / h, 2)}ч 
        ({round(AVERAGE_DAY[activity] / ALL_EXPERIMENT_TIME * 100, 1)}%)""")

    ax = list(axs.items())
    x = [1]
    days = 1

    # First plot - distribution for all days
    def bar_constructor(x, y):
        global offset

        offset += y
        if activity[0] == 'Void':
            return
        ax[0][1].barh(x, y, height=1, left=offset - y, edgecolor="black", linewidth=.5, label=activity[-1],
                      color=ACTIVITIES[activity[0]])
        if y >= .9 * h:
            ax[0][1].text((y / 2 + offset - y), x,
                          f"{round(y / h) if round(y / h, 1) == round(y / h) else round(y / h, 1)}ч", va="center",
                          ha="center", clip_on=True)

    # generate all parts and add it to plot
    for i in range(len(steps)):
        activity = steps[i]

        next_activity_time = dt.fromtimestamp(steps[i + 1][1]) if i != len(steps) - 1 \
            else dt.utcfromtimestamp(dt.now().timestamp())

        this_activity_time = dt.fromtimestamp(activity[1])

        activity_max_time = dt.strptime(dt.fromtimestamp(activity[1]).date().strftime('%Y-%m-%d') + ' 23:59:59', "%Y-%m-%d %H:%M:%S")
        activity_min_time = dt.strptime(dt.fromtimestamp(activity[1]).date().strftime('%Y-%m-%d') + ' 00:00:00', "%Y-%m-%d %H:%M:%S")

        # first bar
        if not i:
            offset = (this_activity_time - activity_min_time).total_seconds()

        # create one bar
        if activities_times[activity[0]][0] <= 24 * h - offset:
            bar_constructor(days, activities_times[activity[0]][0])

        else:
            to_distribute = activities_times[activity[0]][0]
            to_distribute -= 24 * h - offset
            bar_constructor(days, 24 * h - offset)

            # create bars, separated by days
            while to_distribute != 0:
                x.append(len(x) + 1)
                days += 1
                offset = 0

                if to_distribute >= 24 * h:
                    bar_constructor(days, 24 * h)
                    to_distribute -= 24 * h
                else:
                    bar_constructor(days, to_distribute)
                    to_distribute = 0

        activities_times[activity[0]].pop(0)
    # frame by last 2 weeks if not FULL
    start_hour = EXPERIMENT_START_TIME % (24 * 3600) + UTC_OFFSET
    view_shift = ceil((ALL_EXPERIMENT_TIME + start_hour) // (24 * h)) - 13.5 if ceil(
        ALL_EXPERIMENT_TIME // (7 * 24 * h)) > 2 else 0
    ax[0][1].set_yticks(x, [DAYS_OF_WEEK[(i + START_DAY) % 7] for i in range(len(x))])
    ax[0][1].set_ylim(0 if FULL else view_shift, len(x) + .5 if FULL else 15 + view_shift)
    ax[0][1].invert_yaxis()
    ax[0][1].set_xlim(0, 24 * h)
    ax[0][1].set_xticks([i * 864 for i in range(0, 101, 10)], [f"{i}%" for i in range(0, 101, 10)])

    ax[0][1].yaxis.set_major_formatter(lambda y, _: DAYS_OF_WEEK[(int(y - .5) + START_DAY) % 7])
    ax[0][1].xaxis.set_major_formatter(
        lambda x, _: f"{round(x / h) if round(x / h, 1) == round(x / h) else round(x / h, 1)}ч")

    def format_coord(x, y):
        x = round(x / h) if round(x / h, 1) == round(x / h) else round(x / h, 1)
        y = (int(y - .5))

        timestamp = y * 24 * h + x * h + EXPERIMENT_START_TIME - EXPERIMENT_START_TIME % (24 * h) - UTC_OFFSET
        note = ''

        week = f"({round((timestamp - EXPERIMENT_START_TIME) // (7 * 24 * h) + 1)} неделя)"
        if not steps[0][1] <= timestamp <= dt.now().timestamp():
            week = ''

        for i in steps:
            if i[1] >= timestamp or not steps[0][1] <= timestamp <= dt.now().timestamp():
                break
            note = i[-1]

        if note:
            return f"Подпись: {note}\n{x=}ч, y={DAYS_OF_WEEK[(y + START_DAY) % 7]} {week}"
        else:
            return f"\n{x=}ч, y={DAYS_OF_WEEK[(y + START_DAY) % 7]} {week}"

    ax[0][1].format_coord = format_coord

    legend_elements = [*[Patch(facecolor=ACTIVITIES[i], edgecolor="black", linewidth=.5, label=i) for i in AVERAGE_DAY]]
    ax[0][1].legend(handles=legend_elements, ncol=LABELS_IN_ROW, loc="upper left")
    # Second plot - Average time
    offset = 0

    for activity in AVERAGE_DAY:
        ax[1][1].barh(1, AVERAGE_DAY[activity], height=1, edgecolor="black", linewidth=.5, left=offset, label=activity,
                      color=ACTIVITIES[activity])

        if AVERAGE_DAY[activity] >= ALL_EXPERIMENT_TIME * 0.05:
            ax[1][1].text((AVERAGE_DAY[activity] / 2 + offset), 1,
                          f"{round(AVERAGE_DAY[activity] / ALL_EXPERIMENT_TIME * 100, 1)}%", va="center", ha="center",
                          clip_on=True)

        offset += AVERAGE_DAY[activity]

    ax[1][1].set_yticks((1,), ("AV",))
    ax[1][1].set_ylim(.5, 1.5)
    ax[1][1].invert_yaxis()
    ax[1][1].set_xlim(0, ALL_EXPERIMENT_TIME)
    ax[1][1].set_xticks([i * ALL_EXPERIMENT_TIME / 100 for i in range(0, 101, 10)], [f"{i}%" for i in range(0, 101, 10)])
    ax[1][1].yaxis.set_major_formatter(lambda *_: "AV")
    ax[1][1].xaxis.set_major_formatter(mtick.PercentFormatter(ALL_EXPERIMENT_TIME))

    plt.tight_layout()
    # saving image as desired
    # plt.savefig(f"plot.png", bbox_inches="tight")

    plt.show()


def circle_chart(steps):
    data1 = [[0] * len(activities[i][1]) for i in range(2, len(activities) + 1)]
    data1.insert(0, [0])
    for i, it in enumerate(steps):
        t = steps[i + 1][1] if i != len(steps) - 1 else dt.now().timestamp()
        ind = 0
        for j, sp in enumerate(list(activities.values())):
            if it[0][:5] in sp:
                ind = j
        s, s1 = list(activities.keys())[ind], 1
        if s != 1:
            s1 = list(activities[s][1].keys())[list(activities[s][1].values()).index(it[0][6:-1])]
        data1[s - 1][s1 - 1] += t - steps[i][1]
    data = [sum(i) for i in data1]
    data_1 = []
    for i in data1:
        for j in i:
            data_1.append(j)
    plt.pie(data, labels=act, autopct='%1.1f%%', radius=1.5, labeldistance=0.8, wedgeprops=dict(width=0.8))
    plt.pie(data_1, labels=act1, autopct='%1.1f%%', radius=0.7,  labeldistance=0.8)
    plt.show()
