myNum = int(input("Enter a three digit number : "))
if myNum >= 100 :
    tenthDigit = ((myNum%1000)%100)//10
    hundredDigit = (myNum%1000)//100
    result = tenthDigit + hundredDigit
    print(f'The result is {result}')
else:
    print("Enter a number that starts from three digits!")