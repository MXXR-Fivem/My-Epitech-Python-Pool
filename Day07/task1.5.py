def bread():
    print(" <////////// > ")

def lettuce():
    print(" ~~~~~~~~~~~~ ")

def tomato():
    print("O O O O O O")

def ham():
    print(" ============ ")

def makeSandwiches(n: int, isVegan: bool=False) -> None:
    if not isinstance(n, int):
        print("I can't do this !")
        return 
    for _ in range(n):
        bread()
        lettuce()
        tomato()
        if isVegan:
            lettuce()
            tomato()
        else:
            ham()
            ham()
        bread()
        print("\n")

makeSandwiches(1)
makeSandwiches(1, True)