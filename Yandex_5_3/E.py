n1 = int(input())
lst1 = list(set(map(int, input().split())))
n2 = int(input())
lst2 = list(set(map(int, input().split())))
n3 = int(input())
lst3 = list(set(map(int, input().split())))

dic = {}
for i in lst1:
    if dic.get(i) is None:
        dic[i] = 1
    else:
        dic[i] += 1
for i in lst2:
    if dic.get(i) is None:
        dic[i] = 1
    else:
        dic[i] += 1
for i in lst3:
    if dic.get(i) is None:
        dic[i] = 1
    else:
        dic[i] += 1

ans = []
for key, value in dic.items():
    if value >= 2:
        ans.append(key)

print(*sorted(ans))
