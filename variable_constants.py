# anywhere
activities = {
    1: ['sleep'],
    2: ['relax', {1: 'watching_video', 2: 'playing_game', 3: 'other'}],
    3: ['study', {1: 'lyceum', 2: 'schoolwork', 3: 'sirius', 4: 'Codeforces', 5: 'htmlAcademy', 6: 'other'}],
    4: ['other', {1: 'homework', 2: 'programming', 3: 'public_transport', 4: 'other'}]
}
# main
actions = [
    '/stop',
    '/choosing_activity',
    '/create_circle_chart',
    '/create_bar_chart',
    '/delete_last_step',
    '/add_description_to_step',
]
# bar_chart
ACTIVITIES = {
    "sleep": 'blue',
    "relax(watching_video)": 'green',
    "relax(playing_game)": 'yellow',
    'relax(other)': 'orange',
    'study(lyceum)': 'White',
    'study(schoolwork)': 'black',
    'study(sirius)': 'purple',
    'study(Codeforces)': 'pink',
    'study(htmlAcademy)': 'silver',
    "study(other)": 'red',
    'other(homework)': 'lime',
    'other(programming)': 'lime',
    'other(public_transport)': 'brown',
    "other(other)": 'teal',
}
# circle_chart
act = ['sleep', 'relax', 'study', 'other']
act1 = ['sl', 'w_v', 'p_g', 'r_o', 'ly', 'sw', 'sr', 'L_C', 'h_A', 's_o', 'hw', 'pr', 'pt', 'ot']
