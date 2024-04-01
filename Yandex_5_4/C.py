file = open("input.txt")
n, m = map(int, file.readline().split())

arr = list(map(int, file.readline().split()))

pr_sm = [0]*(n + 1)
pr_sm[1] = arr[0]
for i in range(2, n + 1):
    pr_sm[i] = arr[i - 1] + pr_sm[i - 1]
# print(arr)
# print(pr_sm)
for i in range(m):
    l, s = map(int, file.readline().split())
    L = 0
    R = n - 1
    while L < R:
        M = (L + R) // 2
        # print("M =", M, ", arr[M] =", arr[M])
        if arr[M] > s:
            R = M
        else:
            L = M + 1
    flag = False
    if L >= l:
        # print("L =", L)
        for j in range(L - l + 1):
            # print("L =", L, ", l =", l, ", j =", j, "sum =", pr_sm[L - j] - pr_sm[L - l - j], ", s =", s)
            if pr_sm[L - j] - pr_sm[L - l - j] == s:
                print(L - l - j + 1)
                flag = True
                break
            elif pr_sm[L - j] - pr_sm[L - l - j] < s:
                break
        if not flag:
            print(-1)
    else:
        print(-1)
