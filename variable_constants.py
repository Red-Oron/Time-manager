# anywhere
activities = {
    1: ['sleep'],
    2: ['relax', {1: 'watching video', 2: 'playing game', 3: 'other'}],
    3: ['study', {1: 'lyceum', 2: 'schoolwork', 3: 'sirius', 4: 'Codeforces', 5: 'htmlAcademy', 6: 'other'}],
    4: ['other', {1: 'homework', 2: 'programming', 3: 'public transport', 4: 'other'}]
}
# main
actions = {
    'q': 'finish program',
    'w': 'create circle chart',
    'e': 'create barh chart',
    'r': 'delete last step',
    't': 'add description to step',
}
sp = ['q', 'w', 'e', 'r', 't']
# bar_chart
ACTIVITIES = {
    "sleep": 'blue',
    "study(other)": 'red',
    "other(other)": 'teal',
    "relax(watching video)": 'green',
    "relax(playing game)": 'yellow',
    'other(programming)': 'lime',
    'study(sirius)': 'purple',
    'study(htmlAcademy)': 'silver',
    'study(lyceum)': 'White',
    'study(Codeforces)': 'pink',
}
# circle_chart
act = ['sleep', 'relax', 'study', 'other']
act1 = ['sl', 'w_v', 'p_g', 'r_o', 'ly', 'sw', 'sr', 'L_C', 'h_A', 's_o', 'hw', 'pr', 'pt', 'ot']
