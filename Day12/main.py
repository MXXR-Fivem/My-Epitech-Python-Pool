import os, sys, random, time
import pygame as py
from english_words import get_english_words_set

def getRandomWord() -> str:
    randomWord = ""
    if 3 > len(sys.argv) > 1:
        wordListeFile = sys.argv[1]
        try:
            f = open(wordListeFile, "r")
            words = [mot.strip() for mot in f.read().replace(";", "\n").replace(",", "\n").splitlines() if mot.strip()]
            randomWord = random.choice(words)
        except FileNotFoundError:
            print(f"File {wordListeFile} doesn't exist.")
            print("Aleatory word has been selected")
            randomWord = random.choice([*get_english_words_set(['web2'], lower=True)])
    else:
        randomWord = random.choice([*get_english_words_set(['web2'], lower=True)])
    while len(randomWord) > 10 or len(randomWord) < 2:
        randomWord = getRandomWord()
    return randomWord.lower()

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

def getBestScore() -> dict | None:
    try:
        f = open("best_scores.txt", "r")
        lines = f.readlines()
        if not lines:
            return None
        try:
            lastData = lines[-1].strip().split(";")
            return {"word": lastData[0], "time": float(lastData[1]), "penalty": int(lastData[2])}
        except Exception:
            pass
    except FileNotFoundError:
        return None
    
def saveBestScore(word, timeTaken, penalty) -> tuple:
    oldBest = getBestScore()
    if oldBest is None or timeTaken < oldBest["time"]:
        f = open("best_scores.txt", "a")
        f.write(f"{word};{timeTaken};{penalty}\n")
        return oldBest, {"word": word, "time": timeTaken, "penalty": penalty}
    else:
        return oldBest, None

def main() -> None:
    py.init()
    screen = py.display.set_mode((600, 600))
    py.display.set_caption("Hangman game")
    bg_img = py.transform.scale(py.image.load(os.path.join("img", "background.png")), (600, 600))
    stickmanImages = [py.transform.scale(py.image.load(os.path.join("img", img)), (600, 600)) for img in ["2.png", "3.png", "4.png", "5.png", "6.png", "7.png"]]

    font = py.font.SysFont("arial", 24)
    font_small = py.font.SysFont("arial", 22)
    font_big = py.font.SysFont("arial", 28, bold=True)
    winFont = py.font.SysFont("arial", 35, bold=True)

    randomWord = getRandomWord()
    underScoreWord = generateUnderscore(randomWord)

    def create_letters():
        letters = []
        for i, character in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            row = i // 5
            col = i % 5
            x = 395 + col * 47.5
            y = 325 + row * 47.5
            letters.append([x, y, character, True])
        return letters

    letters = create_letters()
    penalty = 0
    showReplay = False
    startTime = time.time()
    timeLimit = 90

    runing = True
    win = False
    timeTaken = 0
    oldBest = None
    newBest = None

    while runing:
        screen.blit(bg_img,(0,0))
        elapsed_time = int(time.time() - startTime)
        remaining_time = max(0, timeLimit - elapsed_time)

        if penalty > 0:
            index = min(penalty - 1, len(stickmanImages))
            screen.blit(stickmanImages[index], (0, 0))

        if underScoreWord.replace(" ", "").lower() == randomWord:
            if not win:
                timeTaken = round(time.time() - startTime, 2)
                oldBest, newBest = saveBestScore(randomWord, timeTaken, penalty)
            win = True
            showReplay = True

        if (remaining_time == 0 or penalty >= 6):
            showReplay = True
            letters = []
        else:
            if not win:
                timer_text = font.render("Remaining time : " + (f"{remaining_time}s" if remaining_time < 60 else f"{(remaining_time//60)}min {remaining_time%60}s"), True, (255, 0, 0) if remaining_time <= 5 else (255, 255, 255))
                screen.blit(timer_text, timer_text.get_rect(topleft=(19.5, 40)))

                penalty_text = font.render(f"Penalties : {penalty}" if penalty > 1 else f"Penalty : {penalty}", True, (255, 0, 0) if penalty >= 5 else (255, 255, 255))
                screen.blit(penalty_text, penalty_text.get_rect(topleft=(20, 75)))

                randomWord_text = font.render(underScoreWord, True, (0, 0, 0))
                screen.blit(randomWord_text, randomWord_text.get_rect(center=(270, 485)))
            else:
                screen.blit(bg_img,(0,0))
                win_text = winFont.render("You win !", True, (0, 255, 0))
                screen.blit(win_text, win_text.get_rect(center=(275, 250)))

                stats_text = font_small.render("Time elapsed : " + (f"{timeTaken//60}min" if (timeTaken//60) >= 1 else "") + f"{timeTaken%60}s | " + (f"Penalties : {penalty}" if penalty > 1 else f"Penalty : {penalty}"), True, (0, 255, 0))
                screen.blit(stats_text, stats_text.get_rect(center=(275, 280 if newBest is not None else 300)))

                if newBest is not None:
                    best_text = font_small.render("New record ! " + (f"({newBest['time']//60}min" if (newBest['time']//60) >= 1 else "") + f"({newBest['time']//60}s | " + (f"{newBest['penalty']} penalties)" if newBest['penalty'] > 1 else f"{newBest['penalty']} penalty)"), True, (0, 255, 0))
                    screen.blit(best_text, best_text.get_rect(center=(275, 310)))

                    if oldBest:
                        old_best_text = font_small.render("Old : " + (f"{oldBest['time']//60}min" if (oldBest["time"]//60) >= 1 else "") + f"{oldBest['time']%60}s | " + (f"{oldBest['penalty']} penalties" if oldBest['penalty'] > 1 else f"{oldBest['penalty']} penalty") + f" with '{oldBest['word']}'", True, (0, 255, 0))
                        screen.blit(old_best_text, old_best_text.get_rect(center=(275, 340)))
                else:
                    if oldBest:
                        best_text = font_small.render("Best : " + (f"{oldBest['time']//60}min" if (oldBest["time"]//60) >= 1 else "") + f"{oldBest['time']%60}s | "  + (f"{oldBest['penalty']} penalties" if oldBest['penalty'] > 1 else f"{oldBest['penalty']} penalty") + f" with '{oldBest['word']}'", True, (0, 255, 0))
                        screen.blit(best_text, best_text.get_rect(center=(275, 340)))

        for event in py.event.get():
            if event.type == py.QUIT:
                runing = False

            pos = py.mouse.get_pos()

            if not showReplay:
                if event.type == py.MOUSEBUTTONDOWN:
                    for letter in letters:
                        x, y, l, visible = letter
                        rect = py.Rect(x-19.5, y-19.5, 27.5, 27.5)
                        if rect.collidepoint(pos) and visible:
                            letter[3] = False
                            underScoreWord = generateUnderscore(randomWord, [x[2] for x in letters if not x[3]])
                            if not l.lower() in randomWord:
                                penalty += 1

                if event.type == py.KEYDOWN:
                    l = event.unicode.upper()
                    for letter in letters:
                        if letter[2] == l and letter[3]:
                            letter[3] = False
                            underScoreWord = generateUnderscore(randomWord, [x[2] for x in letters if not x[3]])
                            if not l.lower() in randomWord:
                                penalty += 1
            else:
                if event.type == py.MOUSEBUTTONDOWN:
                    if replay_button.collidepoint(pos):
                        letters = create_letters()
                        penalty = 0
                        startTime = time.time()
                        showReplay = False
                        win = False
                        randomWord = getRandomWord()
                        underScoreWord = generateUnderscore(randomWord)

        if not showReplay:
            for x, y, l, visible in letters:
                rect = py.Rect(x-19.5, y-19.5, 27.5, 27.5)
                color = (80, 80, 180) if visible else (150, 150, 150)
                py.draw.rect(screen, color, rect, border_radius=5)
                text_surface = font.render(l, True, (0, 0, 0))
                if not visible:
                    text_surface.set_alpha(80)
                screen.blit(text_surface,  text_surface.get_rect(center=(x-7.5, y-7.5)))
        else:
            replay_button = py.Rect(180, 463, 175, 42.5)
            py.draw.rect(screen, (0, 250, 0), replay_button, border_radius=10)
            replay_text = font_big.render("Try again", True, (255, 255, 255))
            screen.blit(replay_text, replay_text.get_rect(center=replay_button.center))

        py.display.update()

    py.quit()

if __name__ == "__main__":
    main()