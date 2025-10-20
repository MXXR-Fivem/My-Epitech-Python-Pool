number = int(input("Enter an integer : "))

if number == 42:
    print("a", end="")
if number <= 21:
    print("b", end="")
if number % 2 == 0:
    print("c", end="")
if (number/2) < 21:
    print("d", end="")
if number %2 != 1 and number >= 45:
    print("e", end="")

if number != 42 and number/2 > 21 and (number %2 != 0 and number < 45):
    print("f")