List1 = [3,5,5,7,8,9]
List2 = [3,3,5,5]
if len(List1) > len(List2):
    for item in List2:
        List2_item = List2.count(item)
        List1_item = List1.count(item)
        if List2_item > List1_item:
            print(f'Not all {List2} appears in {List1}')
            break
        else:
            continue
    else:
        print(f'Yes, {List2} appears in {List1}')
else:
    for item in List1:
        List1_item = List1.count(item)
        List2_item = List2.count(item)
        if List1_item > List2_item:
            print(f'Not all {List1} appears in {List2}')
            break
        else:
            continue
    else:
        print(f'Yes, {List1} appears in {List2}')