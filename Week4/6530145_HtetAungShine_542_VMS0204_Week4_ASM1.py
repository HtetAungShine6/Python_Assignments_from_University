realNum = int(input("Enter number of real numbers : "))
firstHighestNum = 0
secondHighestNum = 0
count = 0
if realNum > 1:
    while realNum > count:
        floatNum = float(input(f'Number#{count+1} :'))
        count += 1
        if floatNum > firstHighestNum:
            secondHighestNum = firstHighestNum
            firstHighestNum = floatNum
        elif floatNum > secondHighestNum:
            secondHighestNum = floatNum
    print(f'The first highest number is : {firstHighestNum}')
    print(f'The second highest number is : {secondHighestNum}')
elif realNum == 0:
    print(f'Enter the value that is greater than 0.')
else:
    newFloatNum = float(input(f'Number#{count+1} : '))
    print(f'The first highest number is : {newFloatNum}')
    print(f'There is no second highest number.')