def rewrite(fileName1: str, fileName2: str) -> None:
    f1 = open(fileName1, "w")
    f2 = open(fileName2, "r")
    f1.writelines(f2)

rewrite("toto.txt", "zen.txt")