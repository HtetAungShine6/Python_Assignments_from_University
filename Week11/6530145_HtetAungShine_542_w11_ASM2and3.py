def easyencrypt(sentence, shift, direction):
    outsen = []
    for i in sentence:
        if i == ' ':
            outsen.append(i)
        else:
            if direction == "right":
                if i.isupper():
                    base = ord('A')
                    encrypt = (ord(i)-base+shift)%26
                    outsen.append(chr(encrypt+base))
                else:
                    base = ord('a')
                    encrypt = (ord(i)-base+shift)%26
                    outsen.append(chr(encrypt+base))
            elif direction == "left":
                if i.isupper():
                    base = ord('A')
                    encrypt = (ord(i)-base+(shift*-1))%26
                    outsen.append(chr(encrypt+base))
                else:
                    base = ord('a')
                    encrypt = (ord(i)-base+(shift*-1))%26
                    outsen.append(chr(encrypt+base))
    return (''.join(outsen))

def easydecrypt(sentence, shift, direction):
    outsen = []
    for i in sentence:
        if i == ' ':
            outsen.append(i)
        else:
            if direction == "right":
                if i.isupper():
                    base = ord('A')
                    decrypt = (ord(i)-base-shift)%26
                    outsen.append(chr(decrypt+base))
                else:
                    base = ord('a')
                    decrypt = (ord(i)-base-shift)%26
                    outsen.append(chr(decrypt+base))
            elif direction == "left":
                if i.isupper():
                    base = ord('A')
                    decrypt = (ord(i)-base-(shift*-1))%26
                    outsen.append(chr(decrypt+base))
                else:
                    base = ord('a')
                    decrypt = (ord(i)-base-(shift*-1))%26
                    outsen.append(chr(decrypt+base))
    return (''.join(outsen))

sen = str(input("Enter a sentence to encrypt and decrypt : "))
shift = int(input("Enter the amount you want to shift : "))
shiftDirection = str(input("Enter the shift direction (right/left) : "))
encryptText = easyencrypt(sen,shift,shiftDirection)
decryptText = easydecrypt(encryptText,shift,shiftDirection)
print(f'The encrypted text is : {encryptText}')
print(f'The decrypted text is : {decryptText}')