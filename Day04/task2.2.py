def stringTwice(string: str) -> str:
    stringTwice = ""
    for elt in string:
        stringTwice += 2*elt
    return stringTwice

print(stringTwice("taxi"))