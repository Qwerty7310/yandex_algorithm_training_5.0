import time
from collections import Counter

import mmh3

start = time.time()

file = open("input.txt")

n = int(file.readline())

arr1 = [[]] * n
for i in range(n):
    lst = [0] * 6
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
    if (sin != 1) and \
            (((min(x1, x2) == x1) and (min(y1, y2) == y2)) or
             ((min(x1, x2) == x2) and (min(y1, y2) == y1))):
        sin *= -1
    lst[4] = ln
    lst[5] = sin
    arr1[i] = lst

arr2 = [[]] * n
for i in range(n):
    lst = [0] * 6
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
    if (sin != 1) and \
            (((min(x1, x2) == x1) and (min(y1, y2) == y2)) or
             ((min(x1, x2) == x2) and (min(y1, y2) == y1))):
        sin *= -1
    lst[4] = ln
    lst[5] = sin
    arr2[i] = lst

dic1 = [[]] * n
for i in range(n):

    ln1 = arr1[i][4]
    sin1 = arr1[i][5]
    x1 = arr1[i][0]
    y1 = arr1[i][1]

    # print(ln1, sin1)
    s = list()
    for j in range(n):
        # if j != i:
        ln2 = arr1[j][4]
        sin2 = arr1[j][5]
        x2 = arr1[j][0]
        y2 = arr1[j][1]
        dist_x = x2 - x1
        dist_y = y2 - y1
        # s.append(tuple([ln2, sin2, dist_x, dist_y]))
        s.append(mmh3.hash64(str(ln2) + str(sin2) + str(dist_x) + str(dist_y)))
    dic1[i] = s

dic2 = [[]] * n
for i in range(n):

    ln1 = arr2[i][4]
    sin1 = arr2[i][5]
    x1 = arr2[i][0]
    y1 = arr2[i][1]
    s = list()
    for j in range(n):
        # if j != i:
        ln2 = arr2[j][4]
        sin2 = arr2[j][5]
        x2 = arr2[j][0]
        y2 = arr2[j][1]
        dist_x = x2 - x1
        dist_y = y2 - y1
        # s.append(tuple([ln2, sin2, dist_x, dist_y]))
        s.append(mmh3.hash64(str(ln2) + str(sin2) + str(dist_x) + str(dist_y)))
#   print(s)
    dic2[i] = s

# for i in dic1:
#     for j in i:
#         print(j)
#     print()
# for i in dic2:
#     print(i)
# print(dic2)
mx = 0
for i in range(n):
    if i % 100 == 0:
        print(i)
    for j in range(n):
        mx = max(mx, len(Counter(dic1[i]) & Counter(dic2[j])))
print(n - mx)

end = time.time()
print(end - start)
