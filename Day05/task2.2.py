print([x + 10 for x in [3, 2, 6, 7, 1, 4]])

# It's the same as :

lst = [3, 2, 6, 7, 1, 4]
for i in range(len(lst)):
    lst[i] += 10

print(lst)

# This code add 10 to each element of the list