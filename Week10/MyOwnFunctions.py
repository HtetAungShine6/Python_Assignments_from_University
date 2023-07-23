def SplitType(numlist):
    int_list = []
    float_list = []
    for n in numlist:
        if isinstance(n, int):
            int_list.append(n)
        else:
            float_list.append(n)
    return int_list, float_list

def ListofOdd(numlist):
    if not numlist:
        return []
    else:
        element = numlist[0]
        if element % 2 != 0:
            return [element] + ListofOdd(numlist[1:])
        else:
            return ListofOdd(numlist[1:])

def KeepTwoDup(numlist):
    outlist = []
    for i in numlist:
        if outlist.count(i) < 2:
            outlist.append(i)
    return outlist