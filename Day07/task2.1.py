def sumOfIntegers(n: int) -> int:
    if n == 0:
        return 0
    return n + sumOfIntegers(n-1)

print(sumOfIntegers(42))