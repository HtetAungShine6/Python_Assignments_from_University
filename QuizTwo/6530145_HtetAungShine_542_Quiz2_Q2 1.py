ListA = [[1, 6], [5, 1], [15, 1], [13, 5, -2]]
ListB = [[2, 1], [4, 3], [-2, 2], [11, 0, 40]]
print(f'ListA : {ListA}')
print("+")
print(f'ListB : {ListB}')
print("=")
result = []
for i in range(len(ListA)):
    sublist = []
    for j in range(len(ListA[i])):
        sum = ListA[i][j] + ListB[i][j]
        sublist.append(sum)
    result.append(sublist)
print(f'Output : {result}')