A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
B = 'DEFGHIJKLMNOPQRSTUVWXYZABC'

message = input("Enter a message : ")
output = ""
for c in message:
    if c.isalpha():
        swap = A.index(c.upper())
        output += B[swap]
    else:
        output += c
print(f'Output : {output}')