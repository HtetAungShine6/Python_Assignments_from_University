 orgList = ['A10', 'BMW3201','Nissan NSX200', 'Benz 220c']
print(f'Original List : {orgList}')
digitList = []
charList = []
for i in orgList:
    secondDigitList = []
    secondCharList = []
    for j in i:
        if j.isdigit():
            secondDigitList.append(j)
            outputDigit = ''.join(secondDigitList)
        else:
            secondCharList.append(j)
            outputChar = ''.join(secondCharList)
    digitList.append(outputDigit)
    charList.append(outputChar)
print(f'List of digits : {digitList}')
print(f'List of chars : {charList}')