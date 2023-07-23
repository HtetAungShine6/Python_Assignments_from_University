num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
remainder1 = num1 % num3 
remainder2 = num2 % num3
if remainder1 == 0 and remainder2 == 0:
    if (num3%2) == 0:
        print("num3 is a factor of both num1 and num2.  Also, num3 is an even number.")
    else:
        print("num3 is a factor of both num1 and num2.  Also, num3 is an odd number.")
if remainder1 != 0 and remainder2 == 0:
    if (num3%2) == 0:
        print("num3 is a factor of num2 only. Also, num3 is an even number.")
    else:
        print("num3 is a factor of num2 only. Also, num3 is an odd number.")
if remainder1 == 0 and remainder2 != 0:
    if (num3%2) == 0:
        print("num3 is a factor of num1 only. Also, num3 is an even number.")
    else:
        print("num3 is a factor of num1 only. Also, num3 is an odd number.")
if remainder1 != 0 and remainder2 != 0:
    if (num3%2) == 0:
        print("num3 is neither a factor of num1 nor num2. Also, num3 is an even number.")
    else:
        print("num3 is neither a factor of num1 nor num2. Also, num3 is an odd number.")