import time

start = time.time()

file = open("input.txt")

n = int(file.readline())

arr1 = [[]]*n
for i in range(n):
    lst = list(map(int, file.readline().split()))
    arr1[i] = lst

arr2 = [[]] * n
for i in range(n):
    lst = list(map(int, file.readline().split()))
    arr2[i] = lst

dic1 = {}
for i in range(n):
    ln1 = ((arr1[i][0] - arr1[i][2]) ** 2 + (arr1[i][1] - arr1[i][3]) ** 2) ** (1 / 2)
    sin1 = abs(arr1[i][1] - arr1[i][3]) / ln1
    if (sin1 != 1) and (((min(arr1[i][0], arr1[i][2]) == arr1[i][0]) and (min(arr1[i][1], arr1[i][3]) == arr1[i][3]))
                        or ((min(arr1[i][0], arr1[i][2]) == arr1[i][2]) and (min(arr1[i][1], arr1[i][3]) == arr1[i][1]))):
        sin1 *= -1

    mn1 = min(arr1[i][0], arr1[i][2])
    if mn1 == arr1[i][0]:
        x1 = arr1[i][0]
        y1 = arr1[i][1]
    else:
        x1 = arr1[i][2]
        y1 = arr1[i][3]

    if dic1.get((ln1, sin1)) is None:
        dic1[(ln1, sin1)] = list()

    s = set()
    for j in range(n):
        if j != i:
            mn2 = min(arr1[j][0], arr1[j][2])
            if mn2 == arr1[j][0]:
                x2 = arr1[j][0]
                y2 = arr1[j][1]
            else:
                x2 = arr1[j][2]
                y2 = arr1[j][3]
            dist_x = x2 - x1
            dist_y = y2 - y1

            ln2 = ((arr1[j][0] - arr1[j][2]) ** 2 + (arr1[j][1] - arr1[j][3]) ** 2) ** (1 / 2)
            sin2 = abs(arr1[j][1] - arr1[j][3]) / ln2
            if (sin2 != 1) and (((min(arr1[j][0], arr1[j][2]) == arr1[j][0]) and (min(arr1[j][1], arr1[j][3]) == arr1[j][3])) \
                    or ((min(arr1[j][0], arr1[j][2]) == arr1[j][2]) and (min(arr1[j][1], arr1[j][3]) == arr1[j][1]))):
                sin2 *= -1
            s.add(tuple([ln2, sin2, dist_x, dist_y]))
    dic1[(ln1, sin1)].append(s)

dic2 = {}
for i in range(n):
    ln1 = ((arr2[i][0] - arr2[i][2]) ** 2 + (arr2[i][1] - arr2[i][3]) ** 2) ** (1 / 2)
    sin1 = abs(arr2[i][1] - arr2[i][3]) / ln1
    if (sin1 != 1) and (((min(arr2[i][0], arr2[i][2]) == arr2[i][0]) and (min(arr2[i][1], arr2[i][3]) == arr2[i][3]))
                        or ((min(arr2[i][0], arr2[i][2]) == arr2[i][2]) and (min(arr2[i][1], arr2[i][3]) == arr2[i][1]))):
        sin1 *= -1

    mn1 = min(arr2[i][0], arr2[i][2])
    if mn1 == arr2[i][0]:
        x1 = arr2[i][0]
        y1 = arr2[i][1]
    else:
        x1 = arr2[i][2]
        y1 = arr2[i][3]

    if dic2.get((ln1, sin1)) is None:
        dic2[(ln1, sin1)] = list()

    s = set()
    for j in range(n):
        if j != i:
            mn2 = min(arr2[j][0], arr2[j][2])
            if mn2 == arr2[j][0]:
                x2 = arr2[j][0]
                y2 = arr2[j][1]
            else:
                x2 = arr2[j][2]
                y2 = arr2[j][3]
            dist_x = x2 - x1
            dist_y = y2 - y1

            ln2 = ((arr2[j][0] - arr2[j][2]) ** 2 + (arr2[j][1] - arr2[j][3]) ** 2) ** (1 / 2)
            sin2 = abs(arr2[j][1] - arr2[j][3]) / ln2
            if (sin2 != 1) and (((min(arr2[j][0], arr2[j][2]) == arr2[j][0]) and (min(arr2[j][1], arr2[j][3]) == arr2[j][3])) \
                    or ((min(arr2[j][0], arr2[j][2]) == arr2[j][2]) and (min(arr2[j][1], arr2[j][3]) == arr2[j][1]))):
                sin2 *= -1
            s.add(tuple([ln2, sin2, dist_x, dist_y]))
    dic2[(ln1, sin1)].append(s)

middle = time.time()
print(middle - start)

mx = 0
for key, value in dic2.items():
    if dic1.get(key) is not None:
        mx = 1
        for i in range(len(list(value))):
            for j in range(len(list(dic1[key]))):
                mx = max(mx, len(list(value)[i].intersection(list(dic1[key])[j]))+1)
                # print(len(list(value)[i].intersection(list(dic1[key])[j])))
if mx > n:
    mx = n
print(n - mx)

end = time.time()
print(end - start)
