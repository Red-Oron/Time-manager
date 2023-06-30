from save import steps
from datetime import datetime as dt
from variable_constants import activities, actions, sp, ACTIVITIES
from chart import bar_chart, circle_chart


def an(s):
    from save import steps
    from variable_constants import activities
    if s.isdigit():
        s = int(s)
        if s != 1:
            print()
            for j in range(1, len(activities[s][1]) + 1):
                print(f'{j}: {activities[s][1][j]}')
            n = input('q: go back\n')
            while n != 'q' and int(n) not in activities[s][1]:
                n = input()
            if n != 'q':
                name_step = f'{activities[s][0]}({activities[s][1][int(n)]})'
            else:
                print()
                return
        else:
            name_step = activities[s][0]
        steps.append([name_step, dt.now().timestamp(), ''])
        print(f'{name_step} step is underway')
        s = input(f'please enter "q" to end the {name_step} step\n')
        while s != 'q':
            s = input(f'please enter "q" to end the {name_step} step\n')
        print()
    elif s == 't':
        bar = input()
        steps[-1][-1] = bar
    elif s == 'r':
        if input('y/n\n') == 'y':
            steps.pop(len(steps) - 1)
    elif s == 'w':
        circle_chart(steps)
    elif s == 'e':
        save_activities = set([_[0] for _ in steps])
        for activity in save_activities:
            if activity not in ACTIVITIES:
                print(f"Занятия {activity} нет в списке активностей!\n")
                return
        bar_chart(steps)
    else:
        print()


while True:
    print('choosing activity:')
    for i in range(1, len(activities) + 1):
        print(f'{i}: {activities[i][0]}')
    for i in range(len(sp)):
        print(f'{sp[i]}: {actions[sp[i]]}')
    print()
    st = input()
    if st == 'q':
        break
    an(st)

f = open('save.py', 'w')
f.write('steps = [\n')
for i in steps:
    f.write('\t' + str(i) + ',\n')
f.write(']\n')
f.close()
