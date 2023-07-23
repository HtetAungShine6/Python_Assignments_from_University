a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
for i in range(a,b+1):
    if i%10 == 3 or i%10 == 7:
        print('*', end = ' ')
    elif (i//10)+(i%10) > 7:
        print('%', end = ' ')
    else:
        print(i, end = ' ')