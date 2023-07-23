userInput = str(input("Enter String : "))

uppercase = 0
lowercase = 0
space = 0
for c in userInput:
    if c.isupper():
        uppercase += 1
    elif c.islower():
        lowercase += 1
    elif c == " ":
        space += 1
print(uppercase)
print(lowercase)
print(space)

case_string = ""
for char in userInput:
    if char.isupper():
        case_string += char.lower()
    elif char.islower():
        case_string += char.upper()
    else:
        case_string += char
print(case_string)