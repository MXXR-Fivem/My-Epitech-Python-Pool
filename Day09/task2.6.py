def write(fileName: str) -> None:
    f = open(fileName, "a")
    totalLines = sum(1 for _ in open(fileName, "r"))
    f.write((totalLines > 0 and "\n" or "") + "I'm a new line")

write("toto.txt")