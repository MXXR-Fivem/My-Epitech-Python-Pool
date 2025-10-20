first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]

magic = list(zip ( first_names , last_names [:: -1]))
magic = [* zip ( first_names , last_names [:: -1]) ] # The same

print(magic)
print(magic[0])
print(magic[1][0])
print(magic[1][1])

# zip function create a tuple with an item of each list