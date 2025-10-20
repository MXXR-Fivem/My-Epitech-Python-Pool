def new_division(num: int | float, den: int | float, acc: int=1) -> None:
    print(round(num/den, acc))

new_division(8.4, 13)
new_division(8.4, 13, 6)