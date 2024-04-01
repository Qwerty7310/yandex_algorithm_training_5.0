file = open("input.txt")
n, m = map(int, file.readline().split())
arr = [[0] * (m + 1) for i in range(n + 1)]

line = file.readline()
if line[0] == '#':
    arr[1][1] = 1
for j in range(2, m + 1):
    arr[1][j] = arr[1][j - 1]
    if line[j - 1] == '#':
        arr[1][j] += 1

for i in range(2, n + 1):
    line = file.readline()
    # print(line)
    arr[i][1] = arr[i - 1][1]
    if line[0] == '#':
        arr[i][1] += 1
    for j in range(2, m + 1):
        arr[i][j] = arr[i][j - 1] + arr[i - 1][j] - arr[i - 1][j - 1]
        if line[j - 1] == '#':
            arr[i][j] += 1

L = 1
R = min(n, m) // 3
while L < R:
    M = (L + R + 1) // 2
    # print("M =", M)
    flag_found = False
    for i in range(3 * M, n + 1):
        for j in range(3 * M, m + 1):
            if (arr[i][j] - arr[i][j - 3 * M] - arr[i - 3 * M][j] + arr[i - 3 * M][j - 3 * M] >= 5 * M * M) \
                    and (arr[i][j - M] - arr[i][j - 2 * M] - arr[i - M][j - M] + arr[i - M][j - 2 * M] == M * M) \
                    and (arr[i - M][j] - arr[i - M][j - M] - arr[i - 2 * M][j] + arr[i - 2 * M][j - M] == M * M) \
                    and (arr[i - M][j - M] - arr[i - M][j - 2 * M] - arr[i - 2 * M][j - M] + arr[i - 2 * M][j - 2 * M] == M * M) \
                    and (arr[i - M][j - 2 * M] - arr[i - M][j - 3 * M] - arr[i - 2 * M][j - 2 * M] + arr[i - 2 * M][j - 3 * M] == M * M) \
                    and (arr[i - 2 * M][j - M] - arr[i - 2 * M][j - 2 * M] - arr[i - 3 * M][j - M] + arr[i - 3 * M][j - 2 * M] == M * M):
                flag_found = True
                break
            # print(i, j, flag_found)
        if flag_found:
            break
    # print(flag_found)
    if flag_found:
        L = M
    else:
        R = M - 1
print(L)
