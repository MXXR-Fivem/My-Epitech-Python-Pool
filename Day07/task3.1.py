def funA(s: str, n: int) -> bool:
    return len(s) >= n

def funB(s: str, n: int) -> bool:
    special_characters = "!@#$%^&*()-+?_=,<>/;"
    count = 0
    for character in s:
        if character in special_characters:
            count += 1
    return count == n

def funC(s: str, n: int) -> bool:
    numbers = "0123456789"
    count = 0
    for character in s:
        if character in numbers:
            count += 1
    return count == n

print(funA("abcd", 4))
print(funB("!@$", 5))
print(funC("048967", 6))