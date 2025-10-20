animalsCounts = [['cat', 666], ['dog', 3], ['elephant', 42]]

newList = sorted([sec for elt in animalsCounts for sec in elt \
                if isinstance(sec, int)])

print(newList)