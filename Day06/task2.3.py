l1 = [True , True ]
l2 = [False , False ]
l3 = [True , False ]
l4 = [False , True ]

l1BoothValues = l1[0] and l1[1]
l2BoothValues = l2[0] and l2[1]
l3BoothValues = l3[0] and l3[1]
l4BoothValues = l4[0] and l4[1]

print(l1BoothValues)
print(l2BoothValues)
print(l3BoothValues)
print(l4BoothValues)

l1BoothValues = l1[0] or l1[1]
l2BoothValues = l2[0] or l2[1]
l3BoothValues = l3[0] or l3[1]
l4BoothValues = l4[0] or l4[1]

print(l1BoothValues)
print(l2BoothValues)
print(l3BoothValues)
print(l4BoothValues)