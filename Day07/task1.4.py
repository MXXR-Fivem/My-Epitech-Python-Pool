def bread():
    print(" <////////// > ")

def lettuce():
    print(" ~~~~~~~~~~~~ ")

def tomato():
    print("O O O O O O")

def ham():
    print(" ============ ")

def makeSandwiches(n: int) -> None:
    if not isinstance(n, int):
        print("I can't do this !")
        return 
    for _ in range(n):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()
        print("\n")

makeSandwiches(5)