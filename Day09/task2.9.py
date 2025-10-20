def frequency(fileName: str) -> dict:
    frequencies = {}
    f = open(fileName, "r")
    wordList = f.read().split()
    for word in wordList:
        for character in [" ", ",", ".", ";", ":", "!", "?", "*", "-"]:
            word = word.replace(character, "")
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

print(frequency("zen.txt"))