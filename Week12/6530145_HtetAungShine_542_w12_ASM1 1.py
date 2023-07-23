def LinearSearch(nList, key):
    count = 1
    for i in range(len(nList)):
        if nList[i] == key:
            return True, count
        count += 1
    return False

def BidirectionSearch(nList, key):
    count = 1
    j = len(nList) - 1
    for i in range(len(nList)//2 + 1):
        if nList[i] == key or nList[j] == key:
            return True, count
        count += 1
        j -= 1
    return False

def FourSliceSearch(nList, key):
    count = 1
    n = len(nList) // 4
    s1 = nList[0:n]
    s2 = nList[n:2*n]
    s3 = nList[2*n:3*n]
    s4 = nList[3*n:]
    for i in range(len(s1)):
        if s1[i] == key or s2[i] == key or s3[i] == key or s4[i] == key:
            return True, count
        count += 1
    return False

def fourslicebidirectionSearch(nList, key):
    count = 1
    n = len(nList) // 4
    s1 = nList[0:n]
    s1r = nList[n-1::-1]
    s2 = nList[n:2*n]
    s2r = nList[(2*n)-1:n-1:-1]
    s3 = nList[2*n:3*n]
    s3r = nList[(3*n)-1:(2*n)-1:-1]
    s4 = nList[3*n:]
    s4r = nList[len(nList)-1:(3*n)-1:-1]
    for i in range(len(s1)):
        if s1[i] == key or s2[i] == key or s3[i] == key or s4[i] == key or s1r[i] == key or s2r[i] == key or s3r[i] == key or s4r[i] == key:
            return True, count
        count += 1
    return False,count

key = 14
nList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
print('========================')
print('========Linear==========')
a, b = LinearSearch(nList, key)
if a:
    print(f'It takes {b} loops to find {key}.')
else:
    print(f'{key} is not found in the list.')
    
a, b = BidirectionSearch(nList, key)
print('========================')
print('=====BiDirection========')
if a:
    print(f'It takes {b} loops to find {key}.')
else:
    print(f'{key} is not found in the list.')
    
a, b = FourSliceSearch(nList, key)
print('========================')
print('=======FourSlice========')
if a:
    print(f'It takes {b} loops to find {key}.')
else:
    print(f'{key} is not found in the list.')

a, b = fourslicebidirectionSearch(nList, key)
print('========================')
print('==FourSliceBiDirection==')
if a:
    print(f'It takes {b} loops to find {key}.')
else:
    print(f'{key} is not found in the list.')
