import random
from time import time
from english_words import get_english_words_set
import nltk
from nltk.corpus import wordnet

for name in ["wordnet", "omw-1.4"]:
    try:
        nltk.data.find("corpora/" + name)
    except:
        nltk.download(name, quiet=True)

def result(n: int, word: str="", time: int=0, penaltyLimit: int=12) -> None:
    print(n >= penaltyLimit and \
        f"\nYou loose, the word was '{word}' !\n{n}/{penaltyLimit} " + (n>1 and "penalties" or "penalty") or \
        f"\nYou Win in {time} minutes !\nThe word was '{word}'"
    )

def getRandomWord(customWordList: bool=False) -> str:
    if customWordList:
        fileName = input("Enter the file name : ")
        f = open(fileName, "r")
        wordList = f.read().split(";")
        return random.choice([*wordList])
    return random.choice([*get_english_words_set(['web2'], lower=True)])

def generateUnderscore(string: str, letters: list=[]) -> str:
    if letters != []:
        underscore = ""
        for letter in string:
            if letter.upper() in letters:
                underscore += letter.upper() + " "
            else:
                underscore += "_ "
        return underscore
    return len(string)*"_ "

def startGame() -> None:
    """""
    This hangman game contains thoses features :
    ✓ the number of penalties
    ✓ the length of unknown words
    ✓ the theme of the unknown word (hint)
    ✓ try to find a letter or the word
    ✓ a file containing a word list to pick in
    ✓ a time limit
    """""
    askTime = int(input("Enter the time limit in minutes : "))
    askPenalty = int(input("Enter the maximum of penalties : "))
    askUseFile = input("Do you want to use a custom word list ? (Y/N) : ")
    randomWord = getRandomWord(askUseFile.lower() == "y")
    underscore = generateUnderscore(randomWord)
    askHint = input("Do you want a hint ? (Y/N) : ")

    if askHint.lower() == "y":
        synsets = wordnet.synsets(randomWord)
        synList = []
        for syn in synsets:
            synList.append(syn.definition()) if not randomWord in syn.definition() else None
        print("Theme of the word : ", end="")
        list(synList) == [] and print("No theme found") or print(*synList, sep=" ; ")

    foundLetters, penalty, letters, startTime = 0, 0, [], time()

    while penalty < askPenalty and foundLetters != len(randomWord) and askTime-(time()-startTime)//60 > 0:

        currentTimeRemaining = int(askTime-(time()-startTime)//60)
        print("\n" + underscore + f" {foundLetters}/{len(randomWord)} letters | {penalty}" + (penalty>1 and f"/{askPenalty} penalties" or f"/{askPenalty} penalty"))
        print(f"{currentTimeRemaining} minutes remaining")
        userTry = input("\nEnter a letter or a word : ")
        
        while (len(userTry) < 1 or len(userTry) > 1 or userTry.upper() in letters) and foundLetters != len(randomWord) and penalty < askPenalty:
            if len(userTry) == len(randomWord):
                if userTry.lower() == randomWord:
                    foundLetters = len(randomWord)
                else:
                    penalty += 1
                    if penalty < askPenalty:
                        print(f"The word is not {userTry}.")
                        currentTimeRemaining = int(askTime-(time()-startTime)//60)
                        print("\n" + underscore + f" {foundLetters}/{len(randomWord)} letters | {penalty}" + (penalty>1 and f"/{askPenalty} penalties" or f"/{askPenalty} penalty"))
                        print(f"{currentTimeRemaining} minutes remaining")
                        userTry = input("Enter a letter or a word : ")
            else:
                print(f"You have to write only one letter that you have not ever writed or a word in {len(randomWord)} letters.")
                userTry = input("Enter a letter or a word : ")

        if not userTry.lower() in randomWord and len(userTry) != len(randomWord):
            penalty += 1
            print(f"No {userTry} found.")
        elif foundLetters != len(randomWord):
            foundLetters += randomWord.count(userTry.lower()) if foundLetters != len(randomWord) else 0
            letters.append(userTry.upper())
            underscore = generateUnderscore(randomWord, letters)

    result(penalty if (askTime-(time()-startTime)/60 > 0) else (askPenalty), randomWord, int((time()-startTime)//60), askPenalty)
    
startGame()