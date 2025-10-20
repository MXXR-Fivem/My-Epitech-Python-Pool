def extractDecimalPart(n: int) -> int:
    result = ""
    integer = True
    i = 0
    while i != len(str(n)):
        currentCaracter = str(n)[i]
        if currentCaracter == ".":
            integer = False
        elif not integer:
            result += currentCaracter
        i += 1
    return result

print(extractDecimalPart(12.24))
print(extractDecimalPart(424242.8412))