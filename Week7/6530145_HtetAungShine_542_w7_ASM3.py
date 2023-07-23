userinput = list((input("Input : ").split()))
n = int(input("Enter a value for n : "))
outputlist = []
for i in userinput:
    for j in range(1,n+1):
        outputlist.append(i.upper()+str(j))
print(f'Output : ', end = ' ')
print(" ".join(outputlist))