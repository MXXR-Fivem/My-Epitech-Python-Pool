dictionary = {
    " dalmatians ": 101 ,
    "pi": 3.14 ,
    " beast ": 666 ,
    " life ": 42 ,
    " googol ": 10^100 ,
    " jordan ": 23 ,
    "life , the universe and everything ": 42 ,
    " emergency ": 911 ,
    " euler ": 2.71828
}

maximum = None
for k, v in dictionary.items():
    if not maximum or v > maximum[1]:
        maximum = (k, v)

print(maximum)