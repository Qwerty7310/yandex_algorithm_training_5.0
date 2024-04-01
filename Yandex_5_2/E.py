file = open("input.txt")

n = int(file.readline())

s2 = []
a2 = 0
i2 = 0

s1 = []
a1 = 0
b1 = 0
i1 = 0

# st = set()
# cnt = 0

cnt2 = 0
max_height = 0
cur_height = 0
# flag = False
for i in range(n):
    # st.add(1)
    a, b = map(int, file.readline().split())
    if a - b > 0:
        # flag = True
        # st.add(2)
        max_height = cur_height + a
        cur_height += a - b
        s1.append(i+1)
        if b > b1:
            # st.add(3)
            if b1 != 0:
                # st.add(4)
                s1.pop()
                s1.append(i1 + 1)
            else:
                # st.add(5)
                s1.pop()
            max_height -= a
            cur_height -= a - b
            max_height = cur_height + a1
            cur_height += a1 - b1
            a1 = a
            b1 = b
            i1 = i
    else:
        # cnt += 1
        # st.add(6)
        s2.append(i+1)
        if a > a2:
            # st.add(7)
            if a2 != 0:
                # st.add(8)
                s2.pop()
                s2.append(i2 + 1)
            else:
                # st.add(9)
                s2.pop()
            a2 = a
            i2 = i

if a1 != 0:
    max_height = cur_height + a1
    cur_height = cur_height + a1 - b1
    s1.append(i1+1)

if a2 != 0:
    # st.add(10)
    if cur_height + a2 > max_height:
        # st.add(11)
        max_height = cur_height + a2
    s1.append(i2+1)
# print("s1 =", s1)

print(max_height)
# print(a1)
# print(a2)
print(*s1, *s2)

# print()
# print(st)
# print(cnt)
