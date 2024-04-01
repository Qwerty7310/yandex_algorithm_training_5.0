import math

x = int(input())
y = int(input())
p = int(input())

if y <= 0:
    i = 0
elif p <= 0:
    i = math.ceil(y / x)
elif (x <= p) and (x <= y - x):
    i = -1
elif y <= x:
    i = 1
elif (y < 2*x) and ((p + y)/x >= 3):
    i = -1
else:
    y = y - x
    i = 1
    n = p
    if y <= 0:
        pass
    else:
        prev = 10**10
        for j in range(2000):
            x1 = x
            y1 = y
            n1 = n
            i = 1
            while(1):
                if (y1 == 0) and (n1 <= 0):
                    break
                i += 1
                if (x1 > y1) and (x1 - (n1 - (x1 - y1)) == 0):
                    i = -1
                    break
                if (x1 <= y1) or (
                        (n1 - (x1 - y1))/(x1 - (n1 - (x1 - y1))) >= 1.5 + j*0.001
                ) or (
                        (n1 - (x1 - y1))/(x1 - (n1 - (x1 - y1))) <= 1
                ):
                    y1 -= x1 - n1
                    n1 = p
                else:
                    n1 -= x1 - y1
                    y1 = 0
                    x1 -= n1
                    if x1 <= 0:
                        i = -1
                        break
            if i > prev:
                i = prev
                break
            elif i != -1:
                prev = i
        if i == -1:
            i = 10**10
        i = min(prev, i)
    if i == 10**10:
        i = -1
print(i)
