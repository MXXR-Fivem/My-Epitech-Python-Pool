def allIntegersFromTo(intFrom: int, intTo: int, divisible: int) -> None:
    for i in range(intFrom, intTo-1, -1):
        print(i%7==0 and (str(i) + "\n") or "", end = "")

allIntegersFromTo(1000, 1, 7)