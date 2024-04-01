n = int(input())

s = set()

for i in range(n):
    k = int(input())
    cur_s = set(input().split())
    if i == 0:
        s = cur_s
    else:
        s = s.intersection(cur_s)
s = sorted(s)

print(len(s))
print(*s)

