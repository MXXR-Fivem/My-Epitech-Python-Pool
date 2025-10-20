import os

def read_file(fileName: str, n: int) -> str:
    if not os.path.exists(fileName): raise FileNotFoundError
    f = open(fileName)
    for lineNumber, line in enumerate(f, 1):
        if lineNumber == n:
            return line
    raise FileNotFoundError(f"Line {n} doesn't exist.")

print(read_file("primes.txt", 20000))