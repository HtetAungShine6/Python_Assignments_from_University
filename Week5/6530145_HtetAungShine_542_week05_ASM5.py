numberA = [4, 1, 2, 9, 7, 100, 5, 0, 99, 100] 
numberB = [100, 10, 200, 25, 7, 20]
lowestDiff = float("inf")
for i in range(len(numberA)):
    for j in range(len(numberB)):
        diff = abs(numberA[i]-numberB[j])
        if diff < lowestDiff:
            lowestDiff = diff
for i in range(len(numberA)):
    for j in range(len(numberA)):
        if i == j:
            continue
        else:
            diff = abs(numberA[i]-numberA[j])
            lowestDiff = min(lowestDiff, diff)
for i in range(len(numberB)):
    for j in range(len(numberB)):
        if i == j:
            continue
        else:
            diff = abs(numberB[i]-numberB[j])
            lowestDiff = min(lowestDiff, diff)
print(lowestDiff)