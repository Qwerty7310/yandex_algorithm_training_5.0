import time
start = time.time()
file = open("input.txt")
x, y, n = map(int, file.readline().split())
dic_mn = {}
dic_mx = {}
for i in range(n):
    a, b = map(int, file.readline().split())
    if dic_mn.get(a) is None:
        dic_mn[a] = b
    else:
        if dic_mn[a] > b:
            dic_mn[a] = b
    if dic_mx.get(a) is None:
        dic_mx[a] = b
    else:
        if dic_mx[a] < b:
            dic_mx[a] = b
arr_mx = sorted(dic_mx.items(), key=lambda item: (item[1], item[0]), reverse=True)
arr_mn = sorted(dic_mn.items(), key=lambda item: (item[1], -item[0]))
L = 0
R = x
while L < R:
    M = (L + R) // 2
    j = 0
    left = arr_mx[0][0]
    right = arr_mx[0][0]
    i = 1
    while i < len(arr_mx):
        if (arr_mx[i][0] < left) and (right - arr_mx[i][0] < M):
            left = arr_mx[i][0]
            i += 1
        elif (arr_mx[i][0] > right) and (arr_mx[i][0] - left < M):
            right = arr_mx[i][0]
            i += 1
        elif (arr_mx[i][0] <= right) and (arr_mx[i][0] >= left):
            i += 1
        else:
            break
    if i >= len(arr_mx):
        i -= 1
    j = 0
    while j < len(arr_mn):
        if (arr_mn[j][0] < left) and (right - arr_mn[j][0] < M):
            left = arr_mn[j][0]
            j += 1
        elif (arr_mn[j][0] > right) and (arr_mn[j][0] - left < M):
            right = arr_mn[j][0]
            j += 1
        elif (arr_mn[j][0] <= right) and (arr_mn[j][0] >= left):
            j += 1
        else:
            break
    if j >= len(arr_mn):
        j -= 1
    dif1 = arr_mx[i][1] - arr_mn[j][1]
    left = arr_mn[0][0]
    right = arr_mn[0][0]
    j = 1
    while j < len(arr_mn):
        if (arr_mn[j][0] < left) and (right - arr_mn[j][0] < M):
            left = arr_mn[j][0]
            j += 1
        elif (arr_mn[j][0] > right) and (arr_mn[j][0] - left < M):
            right = arr_mn[j][0]
            j += 1
        elif (arr_mn[j][0] <= right) and (arr_mn[j][0] >= left):
            j += 1
        else:
            break
    if j >= len(arr_mn):
        j -= 1
    i = 0
    while i < len(arr_mx):
        if (arr_mx[i][0] < left) and (right - arr_mx[i][0] < M):
            left = arr_mx[i][0]
            i += 1
        elif (arr_mx[i][0] > right) and (arr_mx[i][0] - left < M):
            right = arr_mx[i][0]
            i += 1
        elif (arr_mx[i][0] <= right) and (arr_mx[i][0] >= left):
            i += 1
        else:
            break
    if i >= len(arr_mx):
        i -= 1
    dif2 = arr_mx[i][1] - arr_mn[j][1]
    dif = min(dif1, dif2)
    if M > dif:
        R = M
    else:
        L = M + 1
print(L)
end = time.time()
print(end - start)
