def my_sum(*args):
    for number in args:
        if not isinstance(number, int):
            raise ValueError
    return sum(args)

print(my_sum(1))
print(my_sum(1, 2, 3))
print(my_sum(-20, -10))
print(my_sum(-20, -10, 5, 5, 10, 10))
print(my_sum(1, "toto"))