userinput = list((input("Input : ").split()))
n = int(input("Enter a value for n : "))
outputlist = []
for i in userinput:
    for j in range(1,n+1):
        if j%2 == 0:
            outputlist.append(i.upper()+str(j))
        else:
            outputlist.append(i.lower()+str(j))
print(f'Output : ', end = ' ')
print(" ".join(outputlist))