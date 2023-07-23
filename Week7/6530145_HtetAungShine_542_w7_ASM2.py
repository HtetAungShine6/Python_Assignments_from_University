userinput = list((input("Input : ").split()))
userinputlist = []
for i in userinput:
    if i not in userinputlist:
        userinputlist.append(i)
    else:
        continue
print(f'Output : ', end = ' ')
print(" ".join(userinputlist))