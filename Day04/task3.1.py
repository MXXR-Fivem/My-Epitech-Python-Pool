def caesarCipher() -> str:
    askString = input("Enter a sentence : ")
    askKey = int(input("Enter the askKey of the encryption : "))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encryptedWord = ""
    for i in range(len(askString)):
        if askString[i] in alphabet:
            encryptedWord += alphabet[(alphabet.find(askString[i])+askKey)%26]
        else:
            encryptedWord += askString[i]
    return encryptedWord

print(caesarCipher())