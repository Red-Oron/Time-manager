from datetime import datetime as dt
from matplotlib import pyplot as plt


def chart(steps):
    activities = ['sleep', 'relax', 'study', 'other']
    activities1 = ['sl', 'w_v', 'p_g', 'r_o', 'ly', 'sw', 'sr', 'L_C', 'OGE', 'h_A', 's_o', 'hw', 'pr', 'pt', 'ot']
    data = [0, 0, 0, 0]
    data1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(steps) - 1, -1, -1):
        if len(steps) == i + 1:
            n = dt.now().timestamp()
        else:
            n = steps[i + 1][1]
        if steps[i][0] == 'sleep':
            data[0] += (n - steps[i][1])
            data1[0] += (n - steps[i][1])
        elif steps[i][0][:5] == 'relax':
            data[1] += (n - steps[i][1])
            if steps[i][0][6] == 'w':
                data1[1] += (n - steps[i][1])
            elif steps[i][0][6] == 'p':
                data1[2] += (n - steps[i][1])
            elif steps[i][0][6] == 'o':
                data1[3] += (n - steps[i][1])
        elif steps[i][0][:5] == 'study':
            data[2] += (n - steps[i][1])
            if steps[i][0][6:8] == 'ly':
                data1[4] += (n - steps[i][1])
            elif steps[i][0][6:8] == 'sc':
                data1[5] += (n - steps[i][1])
            elif steps[i][0][6:8] == 'si':
                data1[6] += (n - steps[i][1])
            elif steps[i][0][6:8] == 'le':
                data1[7] += (n - steps[i][1])
            elif steps[i][0][6:8] == 'OG':
                data1[8] += (n - steps[i][1])
            elif steps[i][0][6:8] == 'ht':
                data1[9] += (n - steps[i][1])
            elif steps[i][0][6:8] == 'ot':
                data1[10] += (n - steps[i][1])
        elif steps[i][0][:5] == 'other':
            data[3] += (n - steps[i][1])
            if steps[i][0][7] == 'o':
                data1[11] += (n - steps[i][1])
            elif steps[i][0][7] == 'r':
                data1[12] += (n - steps[i][1])
            elif steps[i][0][7] == 'u':
                data1[13] += (n - steps[i][1])
            elif steps[i][0][7] == 't':
                data1[14] += (n - steps[i][1])
    activities_1 = [activities1[i] for i in range(len(data1)) if data1[i] != 0]
    data_1 = [i for i in data1 if i != 0]
    plt.pie(data, labels=activities, autopct='%1.1f%%', radius=1.5, labeldistance=0.8, wedgeprops=dict(width=0.8))
    plt.pie(data_1, labels=activities_1, autopct='%1.1f%%', radius=0.7,  labeldistance=0.8)
    plt.show()
