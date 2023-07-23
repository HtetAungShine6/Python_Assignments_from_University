for i in range(31):
    if i >= 10 and i<=15 or i >= 20 and i <= 25:
        print('_', end= ' ')
    else:
        if i % 3 == 0:
            print(i, end = ' ')
        else:
            print("*", end = ' ')