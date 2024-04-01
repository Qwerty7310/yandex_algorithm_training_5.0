n, k = map(int, input().split())
b = list(map(int, input().split()))

max_pr = 0
for i in range(n - 1):
    j = i + 1
    while (j <= i + k) and (j < n):
        if b[j] - b[i] > max_pr:
            max_pr = b[j] - b[i]
        j += 1
print(max_pr)
