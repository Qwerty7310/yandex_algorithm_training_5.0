for i in range(100):
    for j in range(100):
        if i//6 + j//6 + (i % 6 + j % 6)//6 == (i + j)//6:
            print("<", i, ",", j, ">", i//6 + j//6 + (i % 6 + j % 6)//6, (i + j)//6)
        else:
            print("<", i, ",", j, ">", i//6 + j//6 + (i % 6 + j % 6)//6, (i + j)//6, "NO")
