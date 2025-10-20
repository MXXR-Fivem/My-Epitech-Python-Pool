def ship(*args: str, **kwargs: str | int):
    name = ""
    for arg in args:
        name += arg + " "
    print(name)
    for k, v in kwargs.items():
        print(k, ":", v)

ship("Batman", street="Mountain Drive", city="Gotham")
ship("Superman", "The man of steel", apartment="3D", num= 344, street="Clinton Street",
city="Metropolis")