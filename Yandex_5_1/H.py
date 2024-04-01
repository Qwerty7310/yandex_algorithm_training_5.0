L, x1, v1, x2, v2 = map(int, input().split())

if (x1 == x2) or (x1 == L - x2):
    print("yes")
    print(0)
elif (v1 == 0) and (v2 == 0):
    if (x1 == x2) or (x1 == L - x2):
        print("yes")
        print(0)
    else:
        print("no")
elif (v1 - v2 != 0) and (v1 + v2 != 0):
    s1 = max(x1, x2) - min(x1, x2)
    s2 = L - (max(x1, x2) - min(x1, x2))
    if max(x1, x2) == x1:
        v = v1 - v2
    else:
        v = v2 - v1
    if v > 0:
        t1 = s2 / v
    else:
        t1 = s1 / (-v)

    m1 = (max(x1, x2) - min(x1, x2))/2 + min(x1, x2)
    v_m = (v1 + v2)/2
    if m1 < L/2:
        if v_m > 0:
            t2 = (L/2 - m1)/v_m
        else:
            t2 = m1 / (-v_m)
    else:
        if v_m > 0:
            t2 = (L - m1)/v_m
        else:
            t2 = (m1 - L/2)/(-v_m)

    print("yes")
    print(min(t1, t2))
    # print("1) t1 =", t1)
    # print("1) t2 =", t2)
else:
    print("yes")

    if v1 == v2:
        m1 = (max(x1, x2) - min(x1, x2)) / 2 + min(x1, x2)
        v_m = (v1 + v2) / 2
        if m1 < L / 2:
            if v_m > 0:
                t2 = (L / 2 - m1) / v_m
            else:
                t2 = m1 / (-v_m)
        else:
            if v_m > 0:
                t2 = (L - m1) / v_m
            else:
                t2 = (m1 - L / 2) / (-v_m)
        print(t2)
    else:
        s1 = max(x1, x2) - min(x1, x2)
        s2 = L - (max(x1, x2) - min(x1, x2))
        if max(x1, x2) == x1:
            v = v1 - v2
        else:
            v = v2 - v1
        if v > 0:
            t1 = s2 / v
        else:
            t1 = s1 / (-v)
        print(t1)

    # s1 = abs(x2-x1)/2 + min(x1, x2)
    # if L % 2 == 0:
    #     s2 = (s1 + L//2) % L
    #     if v1 < 0:
    #         t1 = s1/(-v1)
    #         t2 = s2/(-v1)
    #     else:
    #         t1 = (L - s1)/v1
    #         t2 = (L - s2)/v1
    #     print(min(t1, t2))
    # else:
    #     if v1 < 0:
    #         t1 = s1/(-v1)
    #     else:
    #         t1 = (L - s1)/v1
    #     print(t1)

