n = int(input())
arr = list(map(int, input().split()))

max_len = max(arr)

if (arr.count(max_len) > 1) or (sum(arr) - max_len >= max_len):
    print(sum(arr))
else:
    print(max_len - (sum(arr) - max_len))
