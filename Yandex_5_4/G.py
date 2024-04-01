file = open("input25.txt")
n, m = map(int, file.readline().split())
dic = {}
for i in range(n):
    line = file.readline()
    st = 0
    k = 0
    # print('\t', i)
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
        # arr.append([st, k])
    # print()
# for i in dic.items():
#     print(i)
L = 1
R = min(n, m) // 3
# print(L, R)
# print()
while L < R:
    M = (L + R) // 2
    # print("M =", M, ", L =", L, ", R =", R)
    flag = False
    for i in range(n - M):
        flag = False
        for j in range(M, m - 2*M + 1):
            if (dic.get(tuple([i, j])) is not None) and (dic.get(tuple([i, j])) >= M):
                flag = True
                for k in range(M):
                    if (dic.get(tuple([i + k, j])) is None) or (dic[tuple([i + k, j])] < M):
                        # print(i, j, "NO", 1)
                        flag = False
                        break
                if flag:
                    for k in range(M):
                        if (dic.get(tuple([i + M + k, j - M])) is None) or (
                                dic[tuple([i + M + k, j - M])] < M * 3):
                            # print(i, j, "NO", 2, "k =", k)
                            flag = False
                            break
                if flag:
                    for k in range(M):
                        if (dic.get(tuple([i + 2 * M + k, j])) is None) or (dic[tuple([i + 2 * M + k, j])] < M):
                            # print(i, j, "NO", 3)
                            flag = False
                            break
                if flag:
                    # print("V", i, j)
                    break
        if flag:
            break
    # True  - уместилось
    # False - не уместилось
    # print(flag)
    if flag:
        L = M + 1
    else:
        R = M
    # print(L, R)
    # print()
# print(L)
# input()

M = L
# print("/M =", M, ", L =", L, ", R =", R)
flag = False
for i in range(n - M):
    flag = False
    for j in range(M, m):
        if (dic.get(tuple([i, j])) is not None) and (dic.get(tuple([i, j])) >= M):
            flag = True
            for k in range(M):
                if (dic.get(tuple([i + k, j])) is None) or (dic[tuple([i + k, j])] < M):
                    # print(i, j, "NO", 1)
                    flag = False
                    break
            if flag:
                for k in range(M):
                    if (dic.get(tuple([i + M + k, j - M])) is None) or (
                            dic[tuple([i + M + k, j - M])] < M * 3):
                        # print(i, j, "NO", 2, "k =", k)
                        flag = False
                        break
            if flag:
                for k in range(M):
                    if (dic.get(tuple([i + 2 * M + k, j])) is None) or (dic[tuple([i + 2 * M + k, j])] < M):
                        # print(i, j, "NO", 3)
                        flag = False
                        break
            if flag:
                # print("V", i, j)
                break
    if flag:
        break
# True  - уместилось
# False - не уместилось
# print(1, L)
# print('/', flag)
if not flag:
    L -= 1

print(L)
