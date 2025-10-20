def fun1(s: str, n: int) -> bool:
    return len(s) >= n

def fun2(s: str, n: int) -> bool:
    special_characters = "!@#$%^&*()-+?_=,<>/;"
    count = 0
    for character in s:
        if character in special_characters:
            count += 1
    return count == n

def fun3(s: str, n: int) -> bool:
    numbers = "0123456789"
    count = 0
    for character in s:
        if character in numbers:
            count += 1
    return count == n

def passcheck(function: str, n: int, s: str) -> bool:
    return function(s, n)

print(passcheck(fun1, 16, "mysecretpassword"))
print(passcheck(fun2, 3, "mysecretpassword"))
print(passcheck(fun3, 1, "mysecretpassword"))

print(passcheck(fun1, 16, "mysecretpassword!,;1"))
print(passcheck(fun2, 3, "mysecretpassword!,;1"))
print(passcheck(fun3, 1, "mysecretpassword!,;1"))