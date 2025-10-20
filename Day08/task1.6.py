lst = ["Bob", "Emmett", "Gratton", "Mason"]

lst = sorted(lst, key=len, reverse=False)
print(lst)

lst = sorted(lst, key=len, reverse=True)
print(lst)