def sum_of_digits(n: int, n2: int = None) -> int:
    n = n*n2 if n2 is not None else n
    result = 0
    for i in range(len(str(n))):
        result += int(str(n)[i])
    return result

print(sum_of_digits(123456789))
print(sum_of_digits(112233445566778899))
print(sum_of_digits(123456789, 987654321))
print(sum_of_digits(123456789)*sum_of_digits(987654321))