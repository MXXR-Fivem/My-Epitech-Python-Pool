types = {
    "Electric": [],
    "Grass": [],
    "Fire": [],
}

types["Electric"] += ["Pikachu"]
types["Grass"] += ["Bulbausaur", "Leafeaon"]
types["Fire"] += ["Charmander", "Leafaon"]

# First way

for k, v in types.items():
    if "Pikachu" in v:
        print(k)

# Second way

print(next(k for k, v in types.items() if "Pikachu" in v))