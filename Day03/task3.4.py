def askString() -> str:
    sentence = input("Please write a sentence : ")
    word = ""
    newWord = True
    for elt in sentence:
        if newWord:
            word += elt
            newWord = False
        elif elt == " ":
            newWord = True
    return word

print(askString())