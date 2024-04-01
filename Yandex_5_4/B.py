from decimal import Decimal
k_max = 1817118
n = int(input())
L = 0
R = k_max
c = 0
while L < R:
    c += 1
    M = Decimal(str((L + R) // 2))
    sm = Decimal(str(M ** 2 * (1 + M) / 2)) - Decimal(str((M - 1) * M * (M + 1) / 3)) + Decimal(str((1 + M) * M / 2 - 1))
    if sm > n:
        R = M
    else:
        L = M + 1
M = Decimal(str((L + R) // 2))
sm = Decimal(str(M ** 2 * (1 + M) / 2)) - Decimal(str((M - 1) * M * (M + 1) / 3)) + Decimal(str((1 + M) * M / 2 - 1))
if sm > n:
    L -= 1
print(L)

