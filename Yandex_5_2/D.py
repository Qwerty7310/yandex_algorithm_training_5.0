arr = [[0]*8 for i in range(8)]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

p = 0
for i in range(8):
    for j in range(8):
        if arr[i][j] == 1:
            if (i == 0) or (arr[i-1][j] == 0):
                p += 1
            if (i == 7) or (arr[i+1][j] == 0):
                p += 1
            if (j == 0) or (arr[i][j-1] == 0):
                p += 1
            if (j == 7) or (arr[i][j+1] == 0):
                p += 1
print(p)
