from time import timezone

activities = {
    1: ['sleep'],
    2: ['relax', {1: 'watching video', 2: 'playing game', 3: 'other'}],
    3: ['study', {1: 'lyceum', 2: 'schoolwork', 3: 'sirius', 4: 'leetCode', 5: 'OGE', 6: 'other'}],
    4: ['other', {1: 'homework', 2: 'programming', 3: 'public transport', 4: 'other'}]
}
actions = {
    'q': 'finish program',
    'w': 'create circle chart',
    'e': 'create barh chart',
    'r': 'delete last step',
    't': 'add description to step',
}
sp = ['q', 'w', 'e', 'r', 't']

ACTIVITIES = {
    "sleep": 'blue',
    "study(other)": 'red',
    "other(other)": 'navy',
    "relax(watching video)": 'green',
    "relax(playing game)": 'yellow',
    'other(programming)': 'lime',
    'study(sirius)': 'purple',
    'study(OGE)': 'pink',
}

EXCLUDE_VOIDS = False
FULL = False
PLOT_WIDTH = 9
PLOT_HEIGTH = 5.7

PLOT_START_HEIGTH = 2.2
PLOT_START_WIDTH = 3.5

PLOT_HEIGTH_STEP = 0.25
PLOT_WIDTH_STEP = 0.45
LABELS_IN_ROW = len(ACTIVITIES)

s = 1
m = 60
h = 3600

UTC_OFFSET = -timezone
DAYS_OF_WEEK = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
