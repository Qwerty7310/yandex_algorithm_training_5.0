# n = int(input())

file = open("input.txt")
n = int(file.readline())

arr = [[0]*n for i in range(n)]
col = [0]*n
# str_of_el = [0]*n

for i in range(n):
    # a, b = map(int, input().split())
    a, b = map(int, file.readline().split())
    arr[a - 1][b - 1] = 1
    col[b - 1] += 1
    # str_of_el[i] = a - 1
sum_way = [0]*n

# for i in arr:
#     print(i)

for i in range(n):
    for j in range(n):
        sum_way[i] += col[j]*abs(i - j)
min_index = sum_way.index(min(sum_way))

# print()
# print(sum_way)
# print(min_index)

cur_col = [n]*n
for i in range(n):
    if arr[i][min_index] != 1:
        cur_col[i] = i

# print()
# print(cur_col)

cur_way = 0
for i in range(n):
    for j in range(n):
        if (j != min_index) and (arr[i][j] == 1):
            cur_way += abs(i - min(cur_col))
            cur_col[cur_col.index(min(cur_col))] = n
# print("cur_way =", cur_way)

print(sum_way[min_index] + cur_way)
