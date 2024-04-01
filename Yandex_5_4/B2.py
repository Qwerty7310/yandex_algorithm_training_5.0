# import time
# start = time.time()
# k_max = 1817118
# n_max = 10**18
# k = 1
# arr = [[0, 0]]
# while True:
#     sm = 0
#     for i in range(1, k + 1):
#         sm += i * (k - i + 1)
#     sm += int((1 + k) * k / 2 - 1)
#     if sm > n_max:
#         break
#     arr.append([sm, k])
#     k += 600000
# end = time.time()
# print(arr)
# print(end - start)
from decimal import Decimal

arr = [[0, 0], [1, 1], [36000540002000001, 600001], [288002160004000001, 1200001], [972004860006000001, 1800001]]
n = int(input())

L = 0
R = 0
for i in range(len(arr)):
    if n < arr[i][0]:
        L = arr[i-1][1]
        R = arr[i][1]
        break
# L = 0
# R = k_max
c = 0
while L < R:
    c += 1
    M = (L + R) // 2
    sm = 0
    for i in range(1, M + 1):
        sm += Decimal(str(i * (M - i + 1)))
    sm += Decimal(str((1 + M) * M / 2 - 1))
    print(c, '\t', L, R, '\t', sm)

    if sm > n:
        R = M
    else:
        L = M + 1
M = (L + R) // 2
sm = 0
for i in range(1, M + 1):
    sm += Decimal(str(i * (M - i + 1)))
sm += Decimal(str((1 + M) * M / 2 - 1))
if sm > n:
    print("YES")
    L -= 1
# print(L, R)
print(L)
