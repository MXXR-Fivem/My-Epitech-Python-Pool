LanguageFrequencies = {
    "English": {  # English 
        'a':0.082,'b':0.015,'c':0.028,'d':0.043,'e':0.127,'f':0.022,'g':0.020,'h':0.061,'i':0.070,'j':0.0015,'k':0.0077,'l':0.040,'m':0.024,'n':0.067,'o':0.075,'p':0.019,'q':0.00095,'r':0.060,'s':0.063,'t':0.093,'u':0.028,'v':0.010,'w':0.024,'x':0.0015,'y':0.020,'z':0.00074
    },
    "French": {  # French 
        'a':0.076,'b':0.009,'c':0.033,'d':0.037,'e':0.147,'f':0.011,'g':0.010,'h':0.007,'i':0.075,'j':0.006,'k':0.0005,'l':0.055,'m':0.027,'n':0.071,'o':0.058,'p':0.025,'q':0.014,'r':0.065,'s':0.079,'t':0.070,'u':0.063,'v':0.018,'w':0.0004,'x':0.004,'y':0.003,'z':0.001
    },
    "Spanish": {  # Spanish 
        'a':0.125,'b':0.015,'c':0.041,'d':0.050,'e':0.137,'f':0.007,'g':0.010,'h':0.012,'i':0.062,'j':0.004,'k':0.000,'l':0.049,'m':0.031,'n':0.067,'o':0.087,'p':0.025,'q':0.010,'r':0.069,'s':0.079,'t':0.046,'u':0.039,'v':0.011,'w':0.000,'x':0.002,'y':0.010,'z':0.005
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
            if closer is None or abs(j[k]-v) < closer[2]:
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