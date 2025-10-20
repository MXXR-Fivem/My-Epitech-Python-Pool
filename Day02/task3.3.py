def extractIntegerPart(n: int) -> int:
    result = ""
    decimal = False
    i = 0
    while not decimal:
        currentCaracter = str(n)[i]
        if currentCaracter == ".":
            break
        result += currentCaracter
        i += 1
    return result

print(extractIntegerPart(12.24))
print(extractIntegerPart(424242.8412))