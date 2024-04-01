file = open("input.txt")
n = int(file.readline())

arr = [[]] * n
for i in range(n):
    arr[i] = list(map(int, file.readline().split()))

mn = 4
ans = []
for i in range(n):
    if i % 100 == 0:
        print(i)
    for j in range(n):
        cnt = 2
        cur_arr = []
        if j != i:
            # Ax = arr[i][0]
            # Ay = arr[i][1]
            # Bx = arr[j][0]
            # By = arr[j][1]
            # Sx = (arr[j][0] + arr[i][0]) / 2
            # Sy = (arr[j][1] + arr[i][1]) / 2
            # ASx = ((arr[j][0] + arr[i][0]) / 2 - arr[i][0])
            # ASy = ((arr[j][1] + arr[i][1]) / 2 - arr[i][1])
            # SCx = -ASy
            # SCy = ASx
            # SDx = ASy
            # SDy = -ASx
            Cx = (arr[j][0] + arr[i][0]) / 2 - ((arr[j][1] + arr[i][1]) / 2 - arr[i][1])
            Cy = (arr[j][1] + arr[i][1]) / 2 + ((arr[j][0] + arr[i][0]) / 2 - arr[i][0])
            Dx = (arr[j][0] + arr[i][0]) / 2 + ((arr[j][1] + arr[i][1]) / 2 - arr[i][1])
            Dy = (arr[j][1] + arr[i][1]) / 2 - ((arr[j][0] + arr[i][0]) / 2 - arr[i][0])
            if (int(Cx) == Cx) and (int(Cy) == Cy) and (int(Dx) == Dx) and (int(Dy) == Dy):
                    # and (Cx >= - 10 ** 9) and (Cx <= 10 ** 9) \
                    # and (Dx >= - 10 ** 9) and (Dx <= 10 ** 9) \
                    # and (Cy >= - 10 ** 9) and (Cy <= 10 ** 9) \
                    # and (Dy >= - 10 ** 9) and (Dy <= 10 ** 9):
                C = [int(Cx), int(Cy)]
                D = [int(Dx), int(Dy)]

                if C in arr:
                    cnt -= 1
                else:
                    cur_arr.append(C)

                if D in arr:
                    cnt -= 1
                else:
                    cur_arr.append(D)
                if cnt <= mn:
                    mn = cnt
                    ans = cur_arr
                    # file2.write(str(cur_arr[0]) + ' ' + str(cur_arr[1]) + '\n')

print(mn)
if mn:
    for i in ans:
        print(*i)
