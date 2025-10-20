from random import randint
from time import time

def quickSort(lst: list) -> list:
    if lst == []:
        return []
    first = lst[0]
    smaller = quickSort([i for i in lst[1:] if i < first])
    higher = quickSort([i for i in lst[1:] if i >= first])
    return smaller + [first] + higher

randomLst = []
for i in range(1000000):
    randomLst.append(randint(1, 1000000))

start = time()
print(quickSort(randomLst))
print("Time : " + str(time()-start))