m, n = map(int, input().split())
arr = [""]*m
for i in range(m):
    arr[i] = input()

ans = [[0]*n for i in range(m)]

l = []

cnt = 0
for i in range(m):
    for j in range(n):
        if (arr[i][j] == '#') and (ans[i][j] == 0):
            cnt += 1
            i1 = i
            j1 = j
            while (i1 < m) and (arr[i1][j1] == '#'):
                ans[i1][j1] = cnt
                i1 += 1
            l.append(i1-i)
            # for k in ans:
            #     print(k)
            # print()
flag = False
for i in range(n-1):
    j = 0
    while j < m:
        if ans[j][i] != 0:
            length = l[ans[j][i] - 1]
            # print(i, length)
            if (ans[j][i+1] == ans[j+length-1][i+1])\
                    and ((j == 0) or (ans[j-1][i+1] == 0))\
                    and ((j + length == m) or (ans[j + length][i+1] == 0))\
                    and (ans[j][i+1] != 0):
                flag = True
                l[ans[j][i+1] - 1] = 0
                cnt -= 1
                for k in range(j, j + length):
                    ans[k][i+1] = ans[j][i]
            j += length
        j += 1

# print("\nANSWER:")
# for i in ans:
#     print(i)
# print()
# print("l =", l)
# print("cnt =", cnt)

if (cnt == 1) and (flag or l[0] > 1):
    # print("cnt == 1")
    cnt += 1
    exit_flag = False
    for i in range(m):
        for j in range(n):
            if ans[i][j] != 0:
                if (i == m-1) or (ans[i+1][j] == 0):
                    ans[i][j] = -1
                elif (j == n-1) or (ans[i][j+1] == 0):
                    ans[i][j] = -1
                else:
                    k = j
                    while (k < n) and (ans[i][k] != 0):
                        ans[i][k] = -1
                        k += 1
                exit_flag = True
                break
        if exit_flag:
            break

# for i in ans:
#     print(i)

if cnt != 2:
    ans = [[0] * n for i in range(m)]

    l = []

    cnt = 0
    for i in range(m):
        for j in range(n):
            if (arr[i][j] == '#') and (ans[i][j] == 0):
                cnt += 1
                i1 = i
                j1 = j
                while (j1 < n) and (arr[i1][j1] == '#'):
                    ans[i1][j1] = cnt
                    j1 += 1
                l.append(j1 - j)
                # for k in ans:
                #     print(k)
                # print()
    flag = False
    for i in range(m - 1):
        j = 0
        while j < n:
            if ans[i][j] != 0:
                length = l[ans[i][j] - 1]
                if (ans[i + 1][j] == ans[i + 1][j + length - 1]) \
                        and ((j == 0) or (ans[i + 1][j - 1] == 0)) \
                        and ((j + length == n) or (ans[i + 1][j + length] == 0)) \
                        and (ans[i + 1][j] != 0):
                    flag = True
                    l[ans[i + 1][j] - 1] = 0
                    cnt -= 1
                    for k in range(j, j + length):
                        ans[i + 1][k] = ans[i][j]
                j += length
            j += 1

    # print("\nANSWER 2:")
    # for i in ans:
    #     print(i)
    # print()
    # print("2 l =", l)
    # print("2 cnt =", cnt)

    if (cnt == 1) and (flag or l[0] > 1):
        # print("cnt == 1")
        cnt += 1
        exit_flag = False
        for i in range(m):
            for j in range(n):
                if ans[i][j] != 0:
                    if (i == m - 1) or (ans[i + 1][j] == 0):
                        ans[i][j] = -1
                    elif (j == n - 1) or (ans[i][j + 1] == 0):
                        ans[i][j] = -1
                    else:
                        k = j
                        while (k < n) and (ans[i][k] != 0):
                            ans[i][k] = -1
                            k += 1
                    exit_flag = True
                    break
            if exit_flag:
                break

if cnt == 2:
    print("YES")
    first = 0
    second = 0
    for i in range(len(l)):
        if l[i] != 0:
            first = i+1
            for j in range(i+1, len(l)):
                if l[j] != 0:
                    second = j + 1
                    break
        break
    # print("first =", first)
    # print("second =", second)
    if second == 0:
        second = -1
    for i in range(m):
        s = ""
        for j in range(n):
            if ans[i][j] == 0:
                s += '.'
            elif ans[i][j] == first:
                s += 'a'
            elif ans[i][j] == second:
                s += 'b'
        print(s)
else:
    print("NO")
