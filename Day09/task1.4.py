def my_count(stop: int, start: int=0, step: int=1) -> None:
    if not isinstance(stop, int) or step == 0:
        raise ValueError
    for i in range(start, stop, step):
        print(i)

my_count(100, -100, 42)
my_count(-100, 100, -42)
my_count(-100, 100, 0) # Error with 0
my_count("toto", 100, -42) # Error with "toto"