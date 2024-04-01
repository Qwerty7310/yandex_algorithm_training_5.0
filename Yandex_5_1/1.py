n = 1
m = 1
for i in range(10000):
    # print(str(n)+"/"+str(m))
    print(n / m)
    m += n
    n += m
print(n/m)
print()
print(1.618033988749895)
