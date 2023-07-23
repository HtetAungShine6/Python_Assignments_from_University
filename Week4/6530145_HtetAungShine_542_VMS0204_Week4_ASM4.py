numA = int(input("Enter number A : "))
numB = int(input("Enter number B : "))
if numA < numB:
    multi = numB*5
    total = 0
    while total < multi:
        if numA%3 != 0 or numA%7 != 0:
            print(numA)
        numA += 1
        total += numA
else:
    multi = numA*5
    total = 0
    while total < multi:
        if numB%3 != 0 or numB%7 != 0:
            print(numB)
        numB += 1
        total += numB