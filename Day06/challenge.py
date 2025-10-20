def scrabble(string: str) -> int:
    total = 0
    points = {
        "1" : "AEIOULNSTR",
        "2" : "DG",
        "3" : "BCMP",
        "4" : "FHVWY",
        "5" : "K",
        "8" : "JX",
        "10" : "QZ",
    }
    for caracter in string:
        for k, v in points.items():
            if caracter in v:
                total += int(k)
    return total

print(scrabble(input("Enter a word : ")))