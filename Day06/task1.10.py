superheroes = {
    " Batman " : {
        "id": 1 ,
        " aliases ": ["Bruce Wayne", "Dark knight"] ,
    " location ": {
        " number " : 1007 ,
        " street ": " Mountain Drive ",
        " city ": " Gotham "
        }
    } ,
    " Superman " : {
        "id": 2 ,
        " aliases ": ["Kal -El", "Clark Kent", "The Man of Steel"],
        " location ": {
            " number " : 344 ,
            " street ": " Clinton Street ",
            " apartment ": "3D",
            " city ": " Metropolis "
        }
    },
}

superheroes[" Batman "][" aliases "].append("Caped Crusader")
superheroes["Wolverine"] = {"id": 3, " aliases ": [], "location": {}}

for superheroe in superheroes.keys():
    if superheroes[superheroe][" aliases "]:
        i = 0
        for aliase in superheroes[superheroe][" aliases "]:
            i += 1
            print("    " + aliase + (i == len(superheroes[superheroe][" aliases "]) and "\n" or ""))
    if superheroes[superheroe][" aliases "] == []:
        print(superheroe + ":")

        print("No aliases found.")
