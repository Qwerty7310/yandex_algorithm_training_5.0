import time
from collections import Counter

start = time.time()

file = open("input.txt")

n = int(file.readline())

arr1 = [[]]*n
for i in range(n):
    lst = [0]*6
    x1, y1, x2, y2 = map(int, file.readline().split())
    if x1 == x2:
        if min(y1, y2) == y1:
            lst[0] = x1
            lst[1] = y1
            lst[2] = x2
            lst[3] = y2
        else:
            lst[0] = x2
            lst[1] = y2
            lst[2] = x1
            lst[3] = y1
    else:
        if min(x1, x2) == x1:
            lst[0] = x1
            lst[1] = y1
            lst[2] = x2
            lst[3] = y2
        else:
            lst[0] = x2
            lst[1] = y2
            lst[2] = x1
            lst[3] = y1
    ln = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    sin = abs(x2 - x1) / ln
    if (sin != 1) and\
            (((min(x1, x2) == x1) and (min(y1, y2) == y2)) or
             ((min(x1, x2) == x2) and (min(y1, y2) == y1))):
        sin *= -1
    lst[4] = ln
    lst[5] = sin
    arr1[i] = lst

arr2 = [[]] * n
for i in range(n):
    lst = [0]*6
    x1, y1, x2, y2 = map(int, file.readline().split())
    if x1 == x2:
        if min(y1, y2) == y1:
            lst[0] = x1
            lst[1] = y1
            lst[2] = x2
            lst[3] = y2
        else:
            lst[0] = x2
            lst[1] = y2
            lst[2] = x1
            lst[3] = y1
    else:
        if min(x1, x2) == x1:
            lst[0] = x1
            lst[1] = y1
            lst[2] = x2
            lst[3] = y2
        else:
            lst[0] = x2
            lst[1] = y2
            lst[2] = x1
            lst[3] = y1
    ln = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    sin = abs(x2 - x1) / ln
    if (sin != 1) and\
            (((min(x1, x2) == x1) and (min(y1, y2) == y2)) or
             ((min(x1, x2) == x2) and (min(y1, y2) == y1))):
        sin *= -1
    lst[4] = ln
    lst[5] = sin
    arr2[i] = lst

dic1 = {}
for i in range(n):

    ln1 = arr1[i][4]
    sin1 = arr1[i][5]
    x1 = arr1[i][0]
    y1 = arr1[i][1]
    x2 = arr1[i][2]
    y2 = arr1[i][3]

    if dic1.get((ln1, sin1)) is None:
        dic1[(ln1, sin1)] = list()

    s = list()
    for j in range(n):
        if j != i:
            ln2 = arr1[j][4]
            sin2 = arr1[j][5]
            dist_x = x2 - x1
            dist_y = y2 - y1
            s.append(tuple([ln2, sin2, dist_x, dist_y]))
    # print(s)
    dic1[(ln1, sin1)].append(s)

print()

dic2 = {}
for i in range(n):

    ln1 = arr2[i][4]
    sin1 = arr2[i][5]
    x1 = arr2[i][0]
    y1 = arr2[i][1]
    x2 = arr2[i][2]
    y2 = arr2[i][3]

    if dic2.get((ln1, sin1)) is None:
        dic2[(ln1, sin1)] = list()

    s = list()
    for j in range(n):
        if j != i:
            ln2 = arr2[j][4]
            sin2 = arr2[j][5]
            dist_x = x2 - x1
            dist_y = y2 - y1
            s.append(tuple([ln2, sin2, dist_x, dist_y]))
    # print(s)
    dic2[(ln1, sin1)].append(s)


middle = time.time()


mx = 0
for key, value in dic2.items():
    if dic1.get(key) is not None:
        cur_mx = 1
        for i in range(len(list(value))):
            for j in range(len(list(dic1[key]))):
                cur_mx = max(cur_mx, len(Counter(value[i]) & Counter(dic1[key][j])) + 1)
        if cur_mx > mx:
            mx = cur_mx

if mx > n:
    mx = n
print(n - mx)

end = time.time()
print(end - start)
