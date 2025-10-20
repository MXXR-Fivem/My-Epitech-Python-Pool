alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenereCipher() -> str:
    askString = input("Enter a sentence : ")
    askKey = input("Enter the key of the encryption : ").lower()
    alphabetLower, encryptedWord = alphabet.lower(), ""
    decalage = 0
    for i in range(len(askString)):
        if askString[i] in alphabetLower:
            encryptedWord += alphabetLower[(alphabetLower.find(askString[i])+alphabetLower.find(askKey[(i-decalage)%len(askKey)]))%26]
        elif askString[i] in alphabetLower.upper():
            encryptedWord += alphabetLower[(alphabetLower.upper().find(askString[i])+alphabetLower.find(askKey[(i-decalage)%len(askKey)]))%26].upper()
        else:
            encryptedWord += askString[i]
            decalage += 1
    return encryptedWord

print(vigenereCipher())