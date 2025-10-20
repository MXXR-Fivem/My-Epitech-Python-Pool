numberWrited = {
    0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
    50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
    90: "ninety", 100: "hundred", 1000: "thousand"
}

def challenge(n: int, space: str="") -> str:
    if 1000 <= n < 10000: # [1000:10000[
        return challenge(n//1000) + numberWrited[1000]
    elif 100 <= n < 1000: # [100:1000[
        return challenge(n//100) + numberWrited[100] + (n % 100 and challenge(n % 100, "and") or "")
    elif 20 <= n < 100: # [2:100[
        return space + numberWrited[n - (n % 10)] + challenge(n % 10)
    return space + numberWrited[n]

def countLetters(limit: int) -> None:
    if not isinstance(limit, int):
        raise TypeError
    if limit <= 0: 
        raise ValueError
    countTotal = 0
    for i in range(1, limit+1):
        countTotal += len(challenge(i))
    print("Number :", limit, "\nNumber of character :", countTotal)
    print()

countLetters(5)
countLetters(42)
countLetters(1000)