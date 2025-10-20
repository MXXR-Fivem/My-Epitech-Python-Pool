def my_division(n1: int, n2: int) -> int:
    if not isinstance(n1, int) or not isinstance(n2, int) or n2 == 0:
        raise ValueError
    return n1//n2, n1%n2

print(str(my_division(42, 4)[0]) + "\n" + str(my_division(42, 4)[1]))