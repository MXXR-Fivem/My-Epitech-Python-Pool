lst = [1, 1, 2, 2, 3]
lst2 = ['a', 2, 'a', 2, 'A']

def deleteDuplicatedElements(lst: list) -> list:
    newList = []
    for elt in lst:
        if not elt in newList:
            newList.append(elt)
    return newList

print(deleteDuplicatedElements(lst))
print(deleteDuplicatedElements(lst2))