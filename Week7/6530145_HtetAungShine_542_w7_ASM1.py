userinput = list((input("Enter words : ").split()))
count = 0
for i in userinput:
    if len(i) >= 4 and i[0]+i[1] == i[-1]+i[-2]:
        count += 1
print(f'Number of words that meets the requirement is : {count}')