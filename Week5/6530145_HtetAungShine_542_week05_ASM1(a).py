for i in range(1,10):
    for j in range(1,10):
        if (i*j)%2 == 0:
            print('%2d'% (i*j), end=' ')
        else:
            print("--", end = " ")
    print()