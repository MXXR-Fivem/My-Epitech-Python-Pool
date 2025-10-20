from time import time

def powerFast(n: int, power: int) -> int:
    if power == 1:
        return n
    return n * powerFast(n, power-1)

start = time()
print(powerFast(42, 84))
print(powerFast(42, 168))
print("Time : " + str(time()-start))