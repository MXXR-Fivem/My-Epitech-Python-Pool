def caesarDecrypt() -> str:
    askString = input("Enter a sentence : ")
    askKey = int(input("Enter the key of the encryption : "))
    alphabet, encryptedWord = "abcdefghijklmnopqrstuvwxyz", ""
    for i in range(len(askString)):
        if askString[i] in alphabet:
            encryptedWord += alphabet[(alphabet.find(askString[i])-askKey)%26]
        else:
            encryptedWord += askString[i]
    return encryptedWord

print(caesarDecrypt())