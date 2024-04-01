n = int(input())
arr = list(map(int, input().split()))
a, b, k = map(int, input().split())


min_col = (a - 1) // k
max_col = (b - 1) // k

if max_col - min_col >= n - 1:
    print(max(arr))
else:
    mx = 0
    min_col = min_col % n
    max_col = max_col % n
    if max_col < min_col:
        max_col += n
    for i in range(min_col, max_col + 1):
        if i > n - 1:
            index = i % n
        else:
            index = i
        if arr[index] > mx:
            mx = arr[index]
    arr.append(arr[0])
    arr.pop(0)
    arr = list(reversed(arr))
    for i in range(min_col, max_col + 1):
        if i > n - 1:
            index = i % n
        else:
            index = i
        if arr[index] > mx:
            mx = arr[index]
    if mx == 0:
        mx = arr[0]
    print(mx)

# mx = 0
# for i in range(min_col, max_col):
#     if arr[i] > mx:
#         mx = arr[i]
# start = 0
# if min_col == 0:
#     start = n - 1
# else:
#     start = n - min_col
# for i in range(start, n - max_col - 1, -1):
#     if arr[i] > mx:
#         mx = arr[i]
# if mx == 0:
#     mx = arr[0]
# print(mx)
