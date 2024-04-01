# import time
#
# start = time.time()

file = open("input.txt")

n = int(file.readline())

arr = [[]] * n
for i in range(n):
    lst = [0] * 4
    x1, y1, x2, y2 = map(int, file.readline().split())
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    lst[2] = x
    lst[3] = y
    ln = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    sin = abs(x2 - x1) / ln
    if (sin != 1) and \
            (((min(x1, x2) == x1) and (min(y1, y2) == y2)) or
             ((min(x1, x2) == x2) and (min(y1, y2) == y1))):
        sin *= -1
    lst[0] = ln
    lst[1] = sin
    arr[i] = lst
dic = {}
for i in range(n):
    x1, y1, x2, y2 = map(int, file.readline().split())
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    ln = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
    sin = abs(x2 - x1) / ln
    if (sin != 1) and \
            (((min(x1, x2) == x1) and (min(y1, y2) == y2)) or
             ((min(x1, x2) == x2) and (min(y1, y2) == y1))):
        sin *= -1
    for j in range(n):
        if (arr[j][0] == ln) and (arr[j][1] == sin):
            vec = tuple([x - arr[j][2], y - arr[j][3]])
            if dic.get(vec) is None:
                dic[vec] = 1
            else:
                dic[vec] += 1
mx = 0
for i in dic.keys():
    if dic[i] > mx:
        mx = dic[i]
print(n - mx)

# print()
# end = time.time()
# print(end - start)
