def check_even(n:int) -> bool:
    return n%2 == 0

print(list(filter(check_even, [1, 2, 3, 4, 5, 6])))