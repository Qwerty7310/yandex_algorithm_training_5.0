import time
start = time.time()
file = open("input.txt")
n, m = map(int, file.readline().split())
dic = {}
for i in range(n):
    line = file.readline()
    st = 0
    k = 0
    flag = True
    for j in range(m):
        if line[j] == '#':
            if flag:
                st = j
                flag = False
            k += 1
        elif k != 0:
            for t in range(k):
                dic[tuple([i, st + t])] = k - t
            k = 0
            flag = True
    if k != 0:
        for t in range(k):
            dic[tuple([i, st + t])] = k - t
L = 1
R = min(n, m) // 3
end = time.time()
print(end - start)
while L < R:
    M = (L + R) // 2
    flag = False
    for i in range(n - M):
        flag = False
        for j in range(M, m - 2*M + 1):
            if (dic.get(tuple([i, j])) is not None) and (dic.get(tuple([i, j])) >= M):
                flag = True
                for k in range(M):
                    if (dic.get(tuple([i + k, j])) is None) or (dic[tuple([i + k, j])] < M):
                        flag = False
                        break
                if flag:
                    for k in range(M):
                        if (dic.get(tuple([i + M + k, j - M])) is None) or (
                                dic[tuple([i + M + k, j - M])] < M * 3):
                            flag = False
                            break
                if flag:
                    for k in range(M):
                        if (dic.get(tuple([i + 2 * M + k, j])) is None) or (dic[tuple([i + 2 * M + k, j])] < M):
                            flag = False
                            break
                if flag:
                    break
        if flag:
            break
    if flag:
        L = M + 1
    else:
        R = M
start2 = time.time()
M = L
flag = False
for i in range(n - M):
    flag = False
    for j in range(M, m - 2*M + 1):
        if (dic.get(tuple([i, j])) is not None) and (dic.get(tuple([i, j])) >= M):
            flag = True
            for k in range(M):
                if (dic.get(tuple([i + k, j])) is None) or (dic[tuple([i + k, j])] < M):
                    flag = False
                    break
            if flag:
                for k in range(M):
                    if (dic.get(tuple([i + M + k, j - M])) is None) or (
                            dic[tuple([i + M + k, j - M])] < M * 3):
                        flag = False
                        break
            if flag:
                for k in range(M):
                    if (dic.get(tuple([i + 2 * M + k, j])) is None) or (dic[tuple([i + 2 * M + k, j])] < M):
                        flag = False
                        break
            if flag:
                break
    if flag:
        break
if not flag:
    L -= 1
print(L)
end2 = time.time()
print(end2 - start2)
print()
print(end2 - start)
print(len(dic.items()))
