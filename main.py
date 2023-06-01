from save import steps
import datetime as dt
from constants import activities, actions, sp
from circle_chart import chart
run, step, name_step = True, False, ''


def an(s):
    from save import steps
    from constants import activities
    global step, name_step, run
    if step:
        step = False
    elif s.isdigit():
        s = int(s)
        t = False
        if s != 1:
            print()
            for j in range(1, len(activities[s][1]) + 1):
                print(f'{j}: {activities[s][1][j]}')
            print()
            n = input()
            while n != 'r' and int(n) not in activities[s][1]:
                n = input()
            if n != 'r':
                name_step = f'{activities[s][0]}({activities[s][1][int(n)]})'
            else:
                print()
                return
        else:
            name_step = activities[s][0]
        step = True
        steps.append([name_step, dt.datetime.now().timestamp(), ''])
        print(f'{name_step} step is underway')
        s = input()
        while s != 'q':
            s = input('please enter "q"\n')
        an(s)
    elif s == 'w':
        bar = input()
        steps[-1][-1] = bar
    elif s == 'e':
        if input('y/n\n') == 'y':
            steps.pop(len(steps) - 1)
    elif s == 't':
        run = False
    elif s == 'y':
        chart(steps)
    else:
        print()


while run:
    print('choosing activity:')
    for i in range(1, len(activities) + 1):
        print(f'{i}: {activities[i][0]}')
    print()
    for i in range(len(sp)):
        print(f'{sp[i]}: {actions[sp[i]]}')
    print()
    an(input())

f = open('save.py', 'w')
f.write('steps = [\n')
for i in steps:
    f.write('\t' + str(i) + ',\n')
f.write(']\n')
f.close()
