def frequency(fileName: str) -> dict:
    frequencies = {}
    f = open(fileName, "r")
    wordList = f.read().split()
    for word in wordList:
        for character in word:
            if character not in ["", " ", ",", ";", ".", ":", "/", "!", "*", "-"]:
                frequencies[character.lower()] = frequencies.get(character.lower(), 0) + 1
    return frequencies

print(frequency("zen.txt"))