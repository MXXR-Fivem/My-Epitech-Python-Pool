def ask() -> None:
    integer = int(input("Enter a number : "))
    string = str(input("Enter a string : "))
    if integer == 0: return
    if integer >= 42:
        print(integer) 
        return
    for vowel in ["a", "e", "i", "o", "u", "y"]:
        if vowel in string:
            print(integer)
            return
    print(string)

ask()