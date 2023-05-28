from save import steps
import datetime as dt
from constants import activities, actions, sp
run, step, name_step = True, False, ''


def an(s):
    from save import steps
    from constants import activities, actions, sp
    global step, name_step, run
    if step:
        step = False
    if s.isdigit():
        s = int(s)
        step, name_step = True, activities[s - 1]
        steps.append([activities[s - 1], dt.datetime.now().timestamp(), ''])
        print(f'{name_step} step is underway')
        while s != 'q':
            s = input()
        an(s)
    if s == 'w':
        bar = input()
        steps[-1][-1] = bar
    if s == 'e':
        if input('y/n') == 'y':
            steps.pop(len(steps) - 1)
    if s == 'r':
        run = False


while run:
    print('choosing activity:')
    for i in range(len(activities)):
        print(f'{i + 1}: {activities[i]}')
    print()
    for i in range(len(sp)):
        print(f'{sp[i]}: {actions[sp[i]]}')
    an(input())

f = open('save.py', 'w')
f.write('steps = [\n')
for i in steps:
    f.write('\t' + str(i) + ',\n')
f.write(']\n')
f.close()
