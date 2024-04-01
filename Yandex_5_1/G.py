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
    # arr = [0] * 100
    if y <= 0:
        pass
    else:
        while (1):
            if (y == 0) and (n <= 0):
                break
            i += 1
            # if (x <= y) or (
            #         # ( (n - (x - y))/(x - (n - (x - y))) >= 1.6180339887498948482 ) 1.6150627615068
            #         ((n - (x - y)) / (x - (n - (x - y))) >= 1.6120339887498948482)
            #         # and
            #         #     ((n - (x - y)) / (x - (n - (x - y))) <= 1.6180339887498948482)
            #
            #         # ) or (
            #         #         ((n - (x - y)) / (x - (n - (x - y))) < 1.62) and ((n - (x - y)) / (x - (n - (x - y))) > 1.6)
            # ):
            if x - n - y >= 0:
                break
            if (x <= y) or (y == 0) or (x / (n - (x - y)) <= 0.618034):
                # сначала солдат, потом казарму

                if y > 0:
                    y -= x - n
                    n = p
                else:
                    n -= x
                    x -= n
                print("сначала солдат, потом казарму")
            elif x / (n - (x - y)) > 0.618034:
                # сначала казарму, потом солдат
                n -= x - y
                y = 0
                x -= n
                if x <= 0:
                    i = -1
                    break
                print("сначала казарму, потом солдат")

            else:
                i = -1
            print("y =", y)
            print("n =", n)
            print("x =", x)
            input()
        # if i == -1:
        #     arr[j] = 10**10
        # else:
        #     arr[j] = i
    # i = min(arr)
    # if i == 10 ** 10:
    #     i = -1
print(i)
