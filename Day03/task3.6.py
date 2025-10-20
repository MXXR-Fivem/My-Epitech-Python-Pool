LanguageFrequencies = {
    "French": {  # Français
        "a": 0.076, "b": 0.009, "c": 0.033, "d": 0.037, "e": 0.147, "f": 0.011, "g": 0.010,
        "h": 0.008, "i": 0.075, "j": 0.006, "k": 0.0005, "l": 0.055, "m": 0.027, "n": 0.070,
        "o": 0.058, "p": 0.030, "q": 0.014, "r": 0.066, "s": 0.079, "t": 0.070, "u": 0.063,
        "v": 0.018, "w": 0.0005, "x": 0.004, "y": 0.003, "z": 0.001,
        "é": 0.015, "è": 0.003, "ê": 0.003, "ç": 0.001, "à": 0.002, "ù": 0.0005
    },
    "English": {  # English
        "a": 0.082, "b": 0.015, "c": 0.028, "d": 0.043, "e": 0.127, "f": 0.022, "g": 0.020,
        "h": 0.061, "i": 0.070, "j": 0.0015, "k": 0.008, "l": 0.040, "m": 0.024, "n": 0.067,
        "o": 0.075, "p": 0.019, "q": 0.001, "r": 0.060, "s": 0.063, "t": 0.091, "u": 0.028,
        "v": 0.010, "w": 0.024, "x": 0.0015, "y": 0.020, "z": 0.0007
    },
    "Spanish": {  # Español
        "a": 0.125, "b": 0.015, "c": 0.040, "d": 0.050, "e": 0.137, "f": 0.007, "g": 0.010,
        "h": 0.012, "i": 0.062, "j": 0.004, "k": 0.0001, "l": 0.050, "m": 0.030, "n": 0.067,
        "ñ": 0.002, "o": 0.087, "p": 0.025, "q": 0.009, "r": 0.069, "s": 0.079, "t": 0.046,
        "u": 0.039, "v": 0.009, "w": 0.0001, "x": 0.002, "y": 0.010, "z": 0.005
    },
    "Deutsh": {  # Deutsch
        "a": 0.065, "ä": 0.006, "b": 0.019, "c": 0.030, "d": 0.051, "e": 0.174, "f": 0.017,
        "g": 0.030, "h": 0.048, "i": 0.076, "j": 0.003, "k": 0.013, "l": 0.034, "m": 0.025,
        "n": 0.098, "o": 0.026, "ö": 0.003, "p": 0.008, "q": 0.0002, "r": 0.070, "s": 0.073,
        "ß": 0.003, "t": 0.061, "u": 0.044, "ü": 0.006, "v": 0.008, "w": 0.019, "x": 0.0005,
        "y": 0.0005, "z": 0.011
    },
    "Português": {  # Português
        "a": 0.146, "b": 0.010, "c": 0.039, "ç": 0.002, "d": 0.049, "e": 0.126, "f": 0.010,
        "g": 0.013, "h": 0.013, "i": 0.062, "j": 0.004, "k": 0.0001, "l": 0.028, "m": 0.051,
        "n": 0.050, "o": 0.107, "p": 0.025, "q": 0.012, "r": 0.065, "s": 0.078, "t": 0.043,
        "u": 0.046, "v": 0.017, "w": 0.0001, "x": 0.003, "y": 0.0001, "z": 0.004
    },
    "Italian": {  # Italiano
        "a": 0.117, "b": 0.009, "c": 0.045, "d": 0.037, "e": 0.118, "f": 0.011, "g": 0.016,
        "h": 0.015, "i": 0.101, "j": 0.0001, "k": 0.0001, "l": 0.065, "m": 0.025, "n": 0.069,
        "o": 0.098, "p": 0.030, "q": 0.005, "r": 0.064, "s": 0.049, "t": 0.056, "u": 0.031,
        "v": 0.021, "w": 0.0001, "x": 0.0005, "y": 0.0001, "z": 0.012
    }
}

def frequency(string: str) -> dict:
    appa = {}
    freq = {}
    totalOther = 0
    for elt in string.lower():
        if elt in [".", " ", "'", "!", "?", ","]:
            totalOther += 1
        else:
            appa[elt] = appa.get(elt, 0) + 1
    for elt in string.lower():
        if elt not in [".", " ", "'", "!", "?", ","] and (freq == {} or elt not in freq.keys()):
            freq[elt] = freq.get(elt, 0) + appa[elt]/(len(string)-totalOther)
    return freq

def compareEachLetters(freq: dict) -> dict:
    result = {}
    for k, v in freq.items():
        closer = None
        for i, j in LanguageFrequencies.items():
            if k in j.keys() and (closer is None or abs(j[k]-v) < closer[2]):
                closer = (k, i, (abs(j[k]-v)))
        result[closer[0]] = closer[1]
    return result

def countAndAverageLanguage(dictLanguage: dict) -> str:
    dictNumberLanguage = {}
    for k, v in dictLanguage.items():
        dictNumberLanguage[v] = dictNumberLanguage.get(v, 0) + 1
    finalLanguage = None
    for k, v in dictNumberLanguage.items():
        if finalLanguage is None or v > finalLanguage[1]:
            finalLanguage = (k, v)
    return finalLanguage[0]

def frequencyAndLanguage(string: str) -> None:
    freqEachLetters = frequency(string)
    languageofEachLetters = compareEachLetters(freqEachLetters)
    averageLanguage = countAndAverageLanguage(languageofEachLetters)
    print("The frequency of each letters is :")
    for k, v in freqEachLetters.items():
        print("   " + k + " : " + str(v))
    print(f"The language of this text is {averageLanguage}")

frequencyAndLanguage(input("Enter a text : "))