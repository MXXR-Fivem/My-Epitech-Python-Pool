def askString(string: str=None) -> bool:
    if string is None:
        string = input("Enter a word or a sentence : ")
        newWord = ""
        for caracter in string:
            if caracter not in [" ", ".", ":", ";", "!", "?"]:
                newWord += caracter.lower()
        return askString(newWord)
    else:
        if len(string) == 0:
            return True
        elif len(string) %2 != 0:
            return False
        if string[0] == string[-1]:
            return askString(string[1:-1])
        return False
    
print(askString())