def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        base = int(binary[len(binary)-1-i])
        decimal += base * (2 **i )
    return decimal
binaryNumber = str(input("Enter a binary number : "))
if binaryNumber[0] == "0":
    print("The input cannot start with 0!")
else:
    decimalNumber = binary_to_decimal(binaryNumber)
    print(decimalNumber)