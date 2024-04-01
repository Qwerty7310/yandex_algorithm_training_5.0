import math


def barracks(cur_x, cur_y, cur_n, cur_i):
    if cur_x <= 0:
        return 10**10
    elif (cur_y <= 0) and (cur_n <= 0):
        return cur_i
    else:
        cur_i += 1
        cur_n -= cur_x - cur_y
        cur_y = 0
        cur_x -= cur_n

        if (cur_y <= cur_x) and (cur_n <= cur_x):
            if cur_y > 0:
                return min(barracks(cur_x, cur_y, cur_n, cur_i), soldiers(cur_x, cur_y, cur_n, cur_i))
            else:
                return soldiers(cur_x, cur_y, cur_n, cur_i)
        else:
            if cur_x >= cur_y:
                return barracks(cur_x, cur_y, cur_n, cur_i)
            elif cur_x >= cur_n:
                return soldiers(cur_x, cur_y, cur_n, cur_i)
            else:
                return 10**10


def soldiers(cur_x, cur_y, cur_n, cur_i):
    if cur_x <= 0:
        return 10**10
    elif (cur_y <= 0) and (cur_n <= 0):
        return cur_i
    else:
        cur_i += 1
        cur_y -= cur_x - cur_n
        if cur_y > 0:
            cur_n = p
        else:
            cur_n = 0
        if (cur_y <= cur_x) and (cur_n <= cur_x):
            if cur_y > 0:
                return min(barracks(cur_x, cur_y, cur_n, cur_i), soldiers(cur_x, cur_y, cur_n, cur_i))
            else:
                return soldiers(cur_x, cur_y, cur_n, cur_i)
        else:
            if cur_x >= cur_y:
                return barracks(cur_x, cur_y, cur_n, cur_i)
            elif cur_x >= cur_n:
                return soldiers(cur_x, cur_y, cur_n, cur_i)
            else:
                return 10**10


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
        while (1):
            if (n - (x - y))/(x - (n - (x - y))) >= 1.6180339887498948482:
                if (y <= x) and (n <= x):
                    if y > 0:
                        i = min(barracks(x, y, n, i), soldiers(x, y, n, i))
                    else:
                        i = soldiers(x, y, n, i)
                else:
                    if x >= y:
                        i = barracks(x, y, n, i)
                    elif x >= n:
                        i = soldiers(x, y, n, i)
                    else:
                        i = 10 ** 10
                        break
            else:
                break
        if i == 10 ** 10:
            i = -1
print(i)