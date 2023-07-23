startMonth = int(input("Enter a satrting month : "))
startDate = int(input("Enter a satrting date : "))
startDays = int(input("Enter a total number of working days : "))
deadlineMonth = startDays//30
deadline = (startDays%30)+1
if startMonth == 1:
    if deadlineMonth == 1 or deadline != 1:
        print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
    else:
        print(f'The deadline of the project is on month# {(startMonth+deadlineMonth)-1} and deadline is {deadline+29}')
elif deadlineMonth == 2:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 3:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 4:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 5:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 6:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 7:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 8:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 9:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 10:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 11:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')
elif deadlineMonth == 12:
    print(f'The deadline of the project is on month# {startMonth+deadlineMonth} and deadline is {deadline}')