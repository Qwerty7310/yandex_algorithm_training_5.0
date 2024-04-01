dic = set(input().split())
lst2 = list(input().split())

for word in lst2:
    s = ""
    flag = False
    for i in word:
        s += i
        if s in dic:
            print(s, end=' ')
            flag = True
            break
    if not flag:
        print(word, end=' ')
