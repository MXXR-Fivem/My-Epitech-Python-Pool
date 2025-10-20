types = {
    "Electric": [],
    "Grass": [],
    "Fire": [],
}

types["Electric"] += ["Pikachu"]
types["Grass"] += ["Bulbausaur", "Leafeaon"]
types["Fire"] += ["Charmander", "Leafaon"]

print(*types.keys(), sep=", ")