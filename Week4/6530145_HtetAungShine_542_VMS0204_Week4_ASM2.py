num = int(input("Enter a number : "))
reverseNum = 0
while num != 0:
    digit = num % 10
    num //= 10
    reverseNum = reverseNum*10 + digit
print(f'Output number : {reverseNum}')