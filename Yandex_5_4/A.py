file = open("input.txt")
file2 = open("007.a")
ans = list(map(int, file2.readline().split()))

n = int(file.readline())
lst = list(map(int, file.readline().split()))
lst.sort()
# print(lst)
# print()

k = int(file.readline())
for i in range(k):
    a, b = map(int, file.readline().split())
    L = 0
    R = n - 1
    # print("Диапазон:", a, b)
    while L < R:
        M = (L + R) // 2
        if lst[M] >= a:
            R = M
        else:
            L = M + 1
    # print(L, end=' ')
    a1 = L
    # print(a, end=' ')

    # L = 0
    # R = n - 1
    # while L < R:
    #     M = (L + R + 1) // 2
    #     if lst[M] < b:
    #         L = M
    #     else:
    #         R = M - 1
    # print(L, end='\t')
    # b = L

    L = 0
    R = n - 1
    while L < R:
        M = (L + R) // 2
        if lst[M] > b:
            R = M
        else:
            L = M + 1
    if lst[L] > b:
        b1 = L - 1
    else:
        b1 = L
    # print(b, end='\t\t')

    if (a1 == b1) and (lst[b1] < a):
        print(0, end=' ')
        # print("i =", i)
    else:
        print(b1 - a1 + 1, end=' ')
    # print()
    # print()
    # print(i, '\t', b1 - a1 + 1, end=' ')
    # print(b - a + 1, end=' ')
    # if (b - a + 1) != ans[i]:
    #     print("FALSE", ans[i], end='')
    # print()
