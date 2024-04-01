import time

start = time.time()
file = open("input.txt")
n = int(file.readline())

arr = [[]] * n
for i in range(n):
    arr[i] = list(map(int, file.readline().split()))

mn = 4
ans = []
for i in range(n):
    start = time.time()
    for j in range(i + 1, n):
        Ax = arr[i][0]
        Ay = arr[i][1]
        Bx = arr[j][0]
        By = arr[j][1]

        ABx = Bx - Ax
        ABy = By - Ay

        BAx = Ax - Bx
        BAy = Ay - By

        ACx = -ABy
        ACy = ABx

        BDx = BAy
        BDy = -BAx

        Cx = Ax + ACx
        Cy = Ay + ACy

        Dx = Bx + BDx
        Dy = By + BDy
        if (int(Cx) == Cx) and (int(Cy) == Cy) and (int(Dx) == Dx) and (int(Dy) == Dy) \
                and (Cx >= - 10 ** 9) and (Cx <= 10 ** 9) \
                and (Dx >= - 10 ** 9) and (Dx <= 10 ** 9) \
                and (Cy >= - 10 ** 9) and (Cy <= 10 ** 9) \
                and (Dy >= - 10 ** 9) and (Dy <= 10 ** 9):
            C = [int(Cx), int(Cy)]
            D = [int(Dx), int(Dy)]

            if (C in arr) and (D in arr):
                if mn > 0:
                    mn = 0
                    break
            elif C in arr:
                if mn > 1:
                    mn = 1
                    ans = [C]
            elif D in arr:
                if mn > 1:
                    mn = 1
                    ans = [D]
            elif mn > 2:
                mn = 2
                ans = [D, C]

        Ax = arr[i][0]
        Ay = arr[i][1]
        Bx = arr[j][0]
        By = arr[j][1]

        ABx = Bx - Ax
        ABy = By - Ay

        BAx = Ax - Bx
        BAy = Ay - By

        ACx = ABy
        ACy = -ABx

        BDx = -BAy
        BDy = BAx

        Cx = Ax + ACx
        Cy = Ay + ACy

        Dx = Bx + BDx
        Dy = By + BDy
        if (int(Cx) == Cx) and (int(Cy) == Cy) and (int(Dx) == Dx) and (int(Dy) == Dy) \
                and (Cx >= - 10 ** 9) and (Cx <= 10 ** 9) \
                and (Dx >= - 10 ** 9) and (Dx <= 10 ** 9) \
                and (Cy >= - 10 ** 9) and (Cy <= 10 ** 9) \
                and (Dy >= - 10 ** 9) and (Dy <= 10 ** 9):
            C = [int(Cx), int(Cy)]
            D = [int(Dx), int(Dy)]

            if (C in arr) and (D in arr):
                if mn > 0:
                    mn = 0
                    break
            elif C in arr:
                if mn > 1:
                    mn = 1
                    ans = [C]
            elif D in arr:
                if mn > 1:
                    mn = 1
                    ans = [D]
            elif mn > 2:
                mn = 2
                ans = [D, C]
    if mn == 0:
        break
    end = time.time()
    print(end - start)
print(mn)
if mn:
    for i in ans:
        print(*i)
# end = time.time()
# print()
# print(end - start)
