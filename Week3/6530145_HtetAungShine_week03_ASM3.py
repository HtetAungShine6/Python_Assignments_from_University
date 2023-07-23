num = int(input("Enter five digits number : "))

if (num > 9999 and num < 100000):
    firstNum = num // 10000
    secondNum = (num // 1000) % 10
    thirdNum = (num // 100) % 10
    fourthNum = (num // 10) % 10
    fifthNum = num % 10
else:
    print("Wrong input. Try Again.")
    
if (firstNum + secondNum) > (thirdNum + fourthNum + fifthNum):
    fourthNum = 0
    fifthNum = 0
    print(f'The output is {firstNum}{secondNum}{thirdNum}{fourthNum}{fifthNum}')
elif (firstNum + secondNum) < (thirdNum + fourthNum + fifthNum):
    firstNum = 1
    secondNum = 1
    print(f'The output is {firstNum}{secondNum}{thirdNum}{fourthNum}{fifthNum}')
elif (firstNum + secondNum) == (thirdNum + fourthNum + fifthNum):
    if (firstNum % 2) == 0:
        firstNum = 6
    else:
        firstNum = 9
    if (secondNum % 2) == 0:
        secondNum = 6
    else:
        secondNum = 9
    if (thirdNum % 2) == 0:
        thirdNum = 6
    else:
        thirdNum = 9
    if (fourthNum % 2) == 0:
        fourthNum = 6
    else:
        fourthNum = 9
    if (fifthNum % 2) == 0:
        fifthNum = 6
    else:
        fifthNum = 9
    print(f'The output is {firstNum}{secondNum}{thirdNum}{fourthNum}{fifthNum}')