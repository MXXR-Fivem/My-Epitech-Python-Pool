def longest(fileName: str) -> str:
    longestWord = None
    f = open(fileName, "r")
    for line in f:
        currentWord = ""
        for character in line:
            if character in [" ", ",", "!", "?", ".", ";", ":"]:
                currentWord = ""
            else:
                currentWord += character
        if not longestWord or len(currentWord) > longestWord[1]:
            longestWord = (currentWord, len(currentWord))
    return (f"Longest word : {longestWord[0]} ({longestWord[1]} characters)")

print(longest("zen.txt"))