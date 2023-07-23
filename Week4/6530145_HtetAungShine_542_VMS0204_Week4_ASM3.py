enteredNum = ""
even = 0
odd = 0
sumOfEven = 0
sumOfOdd = 0
count = 0
while enteredNum != 0:
    enteredNum = int(input(f'Number#{count+1} : '))
    storedValue = enteredNum
    if storedValue % 2 == 0:
        even += 1
        sumOfEven += enteredNum
    else:
        odd += 1
        sumOfOdd += enteredNum
    count += 1
print(f'Sum of odd numbers : {sumOfOdd}')
print(f'Sum of even numbers {sumOfEven}')
if sumOfOdd > sumOfEven:
    print("The winner is odd numbers.")
elif sumOfEven > sumOfOdd:
    print("The winner is even numbers.")
elif sumOfEven == sumOfOdd:
    print("No winner here. Try again.")