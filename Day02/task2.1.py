def power(maxPower: int, finalpower: int, number:int = 1, result:int = 1) -> int:
    print(number, end=" + ")
    if len(str(number)) == maxPower:
        print(f"{number}\n{maxPower} x 1 result at power {str(finalpower)} is : {str(result ** finalpower)}\n")
        return
    newResult = str(number) + "1"
    power(maxPower, finalpower, newResult, result + int(newResult))

for i in range(1, 6):
    power(11, i)