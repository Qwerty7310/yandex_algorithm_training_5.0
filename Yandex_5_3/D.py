n, k = map(int, input().split())
lst = list(map(int, input().split()))

dic = {}
flag = False
for i in range(n):
    if dic.get(lst[i]) is not None:
        if i - dic.get(lst[i]) <= k:
            print("YES")
            flag = True
            break
        else:
            dic[lst[i]] = i
    else:
        dic[lst[i]] = i
if not flag:
    print("NO")
