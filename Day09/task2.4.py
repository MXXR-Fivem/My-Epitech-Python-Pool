import os

def read_file(fileName: str) -> str:
    if not os.path.exists(fileName): raise FileNotFoundError
    f = open(fileName)
    totalLines = sum(1 for _ in f)
    return totalLines

print(read_file("primes.txt"))