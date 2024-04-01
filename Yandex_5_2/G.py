file = open("input.txt")
t = int(file.readline())

for i in range(t):
    n = int(file.readline())
    lst = list(map(int, file.readline().split()))

    lens = []

    cnt = 0

    max_len = lst[0]
    cur_len = 1
    for j in range(1, n):
        if (cur_len + 1 <= max_len) and (lst[j] >= cur_len + 1):
            cur_len += 1
            max_len = min(max_len, lst[j])
        else:
            lens.append(cur_len)
            cnt += 1
            max_len = lst[j]
            cur_len = 1
    lens.append(cur_len)
    cnt += 1

    print(cnt)
    print(*lens)

