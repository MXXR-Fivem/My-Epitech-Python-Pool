lst = [1, 2, 3, 4, 5]

lst.append(42)
lst.append("forty-two")

lst2 = lst[::-1]

print(lst2[::2], lst[::2])