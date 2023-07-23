nList = [[2,5,99,99], [-3,8,1,2,10], [1, 7,100,10]]
oddList = []
evenList = []
for i in nList:
    secondEvenList = []
    secondOddList = []
    for j in i:
        if j%2 == 0:
            secondEvenList.append(j)
        else:
            secondOddList.append(j)
    if secondEvenList:
        evenList.append(secondEvenList)
    if secondOddList:
        oddList.append(secondOddList)
print(f'Output oddList : {oddList}')
print(f'Output evenList : {evenList}')