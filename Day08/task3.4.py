lst = [-10, 0, 17.6, 28, 100]

def celciusToFahrenheit(temp : float | int) -> float | int:
    return temp * 9/5 + 32

print(list(map(celciusToFahrenheit, lst)))