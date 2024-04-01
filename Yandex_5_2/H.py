file = open("input.txt")
n, m = map(int, file.readline().split())

arr = [[]] * n
for i in range(n):
    arr[i] = list(map(int, file.readline().split()))
file.close()

highs = [[0]*m for i in range(n)]

address = []
max_n = 0
col = 0
num_i = 0
num_j = 0

set_i = set()
set_j = set()

sum_column = [0]*m
sum_string = [0]*n


for i in range(n):
    for j in range(m):
        if arr[i][j] > max_n:
            sum_column = [0] * m
            sum_string = [0] * n
            sum_string[i] += 1
            sum_column[j] += 1

            max_n = arr[i][j]
            address = [[i, j]]
            col = 1
            highs = [[0] * m for i in range(n)]
            highs[i][j] = 1
            num_i = i
            num_j = j

            set_i = set()
            set_i.add(i)
            set_j = set()
            set_j.add(j)
        elif arr[i][j] == max_n:
            sum_string[i] += 1
            sum_column[j] += 1

            highs[i][j] = 1
            address.append([i, j])
            set_i.add(i)
            set_j.add(j)
            col += 1
if col > n + m:
    print(1, 1)
else:
    max_index1 = 0
    max_index2 = 0
    if col > 2:
        if (len(set_i) == 1) or (len(set_j) == 1):
            if len(set_i) == 1:
                max_index1 = list(set_i)[0]
                cur_max = 0
                cur_i = 0
                cur_j = 0
                for i in range(n):
                    if i != max_index1:
                        for j in range(m):
                            if arr[i][j] > cur_max:
                                cur_max = arr[i][j]
                                cur_i = i
                                cur_j = j
                max_index2 = cur_j
                print(max_index1, max_index2)
            else:
                max_index2 = list(set_j)[0]
                cur_max = 0
                cur_i = 0
                cur_j = 0
                for i in range(n):
                    for j in range(m):
                        if (j != max_index2) and (arr[i][j] > cur_max):
                            cur_max = arr[i][j]
                            cur_i = i
                            cur_j = j
                print(max_index1, max_index2)
        else:
            highs_sum = [[0] * m for i in range(n)]
            flag = False
            for i in range(n):
                for j in range(m):
                    if col - sum_string[i] - sum_column[j] + highs[i][j] == 0:
                        print(i + 1, j + 1)
                        flag = True
                        break
                if flag:
                    break

            if not flag:
                print(1, 1)
    elif col == 2:
        if (len(set_i) == 1) or (len(set_j) == 1):
            if len(set_i) == 1:
                max_index1 = list(set_i)[0]
                cur_max = 0
                cur_i = 0
                cur_j = 0
                for i in range(n):
                    if i != max_index1:
                        for j in range(m):
                            if arr[i][j] > cur_max:
                                cur_max = arr[i][j]
                                cur_i = i
                                cur_j = j
                max_index2 = cur_j
                print(max_index1 + 1, max_index2 + 1)
            else:
                max_index2 = list(set_j)[0]
                cur_max = 0
                cur_i = 0
                cur_j = 0
                for i in range(n):
                    for j in range(m):
                        if (j != max_index2) and (arr[i][j] > cur_max):
                            cur_max = arr[i][j]
                            cur_i = i
                            cur_j = j
                max_index1 = cur_i
                print(max_index1 + 1, max_index2 + 1)
        else:
            max_index1 = 0
            max_index2 = 0
            index = [0, 0]
            type1 = ''
            minimum_max = 10 ** 9 + 1
            for a in address:
                max_adr = [[]] * 3
                cur_max1 = 0
                for i in range(n):
                    for j in range(m):
                        if (i != a[0]) and (j != a[1]) and (arr[i][j] > cur_max1):
                            cur_max1 = arr[i][j]
                            max_adr[0] = [i, j]
                cur_max2 = 0
                for i in range(n):
                    for j in range(m):
                        if (i != a[0]) and (j != max_adr[0][1]) and (arr[i][j] > cur_max2):
                            cur_max2 = arr[i][j]
                            max_adr[1] = [i, j]

                cur_max3 = 0
                for i in range(n):
                    for j in range(m):
                        if (i != max_adr[0][0]) and (j != a[1]) and (arr[i][j] > cur_max3):
                            cur_max3 = arr[i][j]
                            max_adr[2] = [i, j]
                if min(cur_max1, cur_max2, cur_max3) < minimum_max:
                    if min(cur_max1, cur_max2, cur_max3) == cur_max1:
                        index = [a[0], a[1]]
                    elif min(cur_max1, cur_max2, cur_max3) == cur_max2:
                        index = [a[0], max_adr[0][1]]
                    else:
                        index = [max_adr[0][0], a[1]]
            print(index[0] + 1, index[1] + 1)
    else:
        max_index1 = 0
        max_index2 = 0
        index = [0, 0]
        type1 = ''
        minimum_max = 10 ** 9 + 1
        for a in address:
            max_adr = [[]] * 3
            cur_max1 = 0
            for i in range(n):
                for j in range(m):
                    if (i != a[0]) and (j != a[1]) and (arr[i][j] > cur_max1):
                        cur_max1 = arr[i][j]
                        max_adr[0] = [i, j]
            cur_max2 = 0
            for i in range(n):
                for j in range(m):
                    if (i != a[0]) and (j != max_adr[0][1]) and (arr[i][j] > cur_max2):
                        cur_max2 = arr[i][j]
                        max_adr[1] = [i, j]

            cur_max3 = 0
            for i in range(n):
                for j in range(m):
                    if (i != max_adr[0][0]) and (j != a[1]) and (arr[i][j] > cur_max3):
                        cur_max3 = arr[i][j]
                        max_adr[2] = [i, j]
            if min(cur_max1, cur_max2, cur_max3) < minimum_max:
                if min(cur_max1, cur_max2, cur_max3) == cur_max1:
                    index = [a[0], a[1]]
                elif min(cur_max1, cur_max2, cur_max3) == cur_max2:
                    index = [a[0], max_adr[0][1]]
                else:
                    index = [max_adr[0][0], a[1]]
        print(index[0] + 1, index[1] + 1)
