def smallestPositiveNumberDivisibleBy(minNumber: int, maxNumber: int) -> int:
    currentNumber = maxNumber+1
    numberNotFind = True
    while numberNotFind:
        for i in range(minNumber, maxNumber+1):
            if currentNumber%i != 0:
                currentNumber += 1
                break
            elif i == maxNumber:
                numberNotFind = False
    return currentNumber

print(smallestPositiveNumberDivisibleBy(1, 4))

# For small values like ~20 brute force like this is possible but 
# if you want to try with bigger numbers you have to find another solution

# 2nd solution :

from math import gcd # Greatest common divisor
from functools import reduce # Reduce iterable fonction to a single value

def lcm(a: int, b: int) -> int: # Least common multiple
    if a == 0 or b == 0:
        return 0
    return (abs(a*b) // gcd(a, b)) # https://en.wikipedia.org/wiki/Least_common_multiple

def smallestPositiveNumberDivisibleByV2(maxIteration: int) -> str:
    return (str(maxIteration) + " : " + str(reduce(lcm, (_ for _ in range(1, maxIteration+1)))))

for i in [4, 7, 20, 200, 2000, 4000]:
    print(smallestPositiveNumberDivisibleByV2(i))

# 3rd solution :

from math import lcm # Least common multiple
from functools import reduce # Reduce iterable fonction to a single value

def gcd(a: int, b: int) -> int: # Greatest / Highest common multiple
    if a == 0 or b == 0:
        return 0
    return (abs(a*b) // lcm(a, b)) # https://en.wikipedia.org/wiki/Least_common_multiple

def smallestPositiveNumberDivisibleByV2(maxIteration: int) -> str:
    return (str(maxIteration) + " : " + str(reduce(lcm, (_ for _ in range(1, maxIteration+1)))))

for i in [4, 7, 20, 200, 2000, 4000]:
    print(smallestPositiveNumberDivisibleByV2(i))