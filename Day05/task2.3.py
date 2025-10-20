lst = [1, 2, 3, 4, 5]

minimum = None
maximum = None
for elt in lst:
    if minimum is None or elt < minimum:
        minimum = elt
    if maximum is None or elt > maximum:
        maximum = elt

print(minimum, maximum, lst)