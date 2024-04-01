n = int(input())

dic = {}

for i in list(map(int, input().split())):
    if dic.get(i) is None:
        dic[i] = 1
    else:
        dic[i] += 1

mx_sm = 0
for k in dic.keys():
    cur_sm = dic[k]
    if dic.get(k - 1) is not None:
        mx_sm = max(mx_sm, dic[k] + dic[k-1])
    elif dic.get(k + 1) is not None:
        mx_sm = max(mx_sm, dic[k] + dic[k + 1])
    else:
        mx_sm = max(mx_sm, dic[k])

print(n - mx_sm)
