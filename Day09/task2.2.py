import os

def read_file(fileName: str) -> None:
    if not os.path.exists(fileName): raise FileNotFoundError(f"File {fileName} doesn't exist.")
    f = open(fileName)
    for line in f:
        print(line, end="")

read_file("zen.txt")
