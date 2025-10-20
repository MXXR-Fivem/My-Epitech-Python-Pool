from collections import Counter 
from time import time

LanguageFrequencies = {
    "English": {
        'a':0.082,'b':0.015,'c':0.028,'d':0.043,'e':0.127,'f':0.022,'g':0.020,'h':0.061,'i':0.070,'j':0.0015,'k':0.0077,'l':0.040,'m':0.024,'n':0.067,'o':0.075,'p':0.019,'q':0.00095,'r':0.060,'s':0.063,'t':0.093,'u':0.028,'v':0.010,'w':0.024,'x':0.0015,'y':0.020,'z':0.00074
    },
}

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decryptVigenereCipher(askString: str, askKey: str) -> str:
    askString = askString
    askKey = askKey.lower()
    alphabetLower, encryptedWord = alphabet.lower(), ""
    decalage = 0
    for i in range(len(askString)):
        if askString[i] in alphabetLower:
            encryptedWord += alphabetLower[(alphabetLower.find(askString[i])-alphabetLower.find(askKey[(i-decalage)%len(askKey)]))%26]
        elif askString[i] in alphabetLower.upper():
            encryptedWord += alphabetLower[(alphabetLower.upper().find(askString[i])-alphabetLower.find(askKey[(i-decalage)%len(askKey)]))%26].upper()
        else:
            encryptedWord += askString[i]
            decalage += 1
    return encryptedWord

def caesarDecrypt(char: str, pos: int) -> str:
    if char in alphabet:
        return alphabet[(alphabet.index(char) - pos) % 26]
    return char

def chiSquaredTest(textSegment: str) -> str:
    """https://en.wikipedia.org/wiki/Chi-squared_test"""
    counts = Counter(textSegment)
    chi2 = 0.0
    for letter in alphabet:
        observed = counts.get(letter, 0)
        expected = LanguageFrequencies["English"][letter.lower()] * len(textSegment)
        chi2 += ((observed - expected) ** 2) / expected if expected > 0 else 0
    return chi2

def bestSegmentPos(segment: str) -> int:
    best_pos = 0
    best_chi2 = float("+inf")
    for pos in range(26):
        decrypted = "".join(caesarDecrypt(character, pos) for character in segment)
        chi2 = chiSquaredTest(decrypted)
        if chi2 < best_chi2:
            best_chi2 = chi2
            best_pos = pos
    return best_pos

def decryptEnglishVigenereCipheredText(vigenereText: str, keylength: int) -> tuple:
    vigenereTextSeg = "".join([character for character in vigenereText.upper() if character in alphabet])
    segments = ["" for _ in range(keylength)]
    for i, v in enumerate(vigenereTextSeg):
        segments[i % keylength] += v

    key_pos = [bestSegmentPos(seg) for seg in segments]
    key = ''.join(alphabet[pos] for pos in key_pos)

    decryptedText = decryptVigenereCipher(vigenereText, key)

    return key, decryptedText

vigenereText = "Gmibgcnmy teb nGmwv poejep fopnxu ko xm yzln xfx igqlr lfjexghe dyv razq zvmuccw !"
KeyLength = 6

key, decryptedText = decryptEnglishVigenereCipheredText(vigenereText, KeyLength)
print(f"Key : {key}\nOriginal text : {decryptedText}")