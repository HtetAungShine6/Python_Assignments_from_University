import MyOwnFunctions
numlist = [1, 2.5, 3, 4.6, 5]
int_list, float_list = MyOwnFunctions.SplitType(numlist)
print("Int List:", int_list)
print("Float List:", float_list)

numlist = [24,32,44,43,55,13,77]
odd_list = MyOwnFunctions.ListofOdd(numlist)
print("Odd List:", odd_list)

numlist = [1, 2, 2, 2, 3, 4, 5, 5, 5, 1, 2, 3, 3]
outlist = MyOwnFunctions.KeepTwoDup(numlist)
print("Out List:", outlist)