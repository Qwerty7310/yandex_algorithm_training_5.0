s1 = input()
s2 = input()
if len(s1) != len(s2):
    print("NO")
elif sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")
