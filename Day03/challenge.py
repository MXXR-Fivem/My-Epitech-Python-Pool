def countOccurence(string: str):
    string = string.lower()
    count = 0
    lst = ["cat", "garden", "mice"]
    for elt in lst:
        count += string.count(elt) + string[::-1].count(elt)
    return count

print(countOccurence("the CataCat attaCk a Cat"))
print(countOccurence("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"))