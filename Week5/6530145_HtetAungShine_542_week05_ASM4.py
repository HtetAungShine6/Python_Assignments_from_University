numbers = [100, 10, 200, 25, 7, 20]
lowestDiff = max(numbers)
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            diff = abs(numbers[i]-numbers[j])
            lowestDiff = min(lowestDiff, diff)
        else:
            continue
print(lowestDiff)