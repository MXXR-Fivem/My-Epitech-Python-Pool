lst = ["apple", "banana", "kiwi", "pear"]

def remove4characters(string: str) -> bool:
    return len(string) > 4

print(list(filter(remove4characters, lst)))