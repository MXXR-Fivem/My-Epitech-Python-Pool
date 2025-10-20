def sixDecimal(precision: int, start:int=7) -> tuple:
    calcul = "4*(1/1-1/3+1/5-1/7+1/"
    for i in range(precision):
        calcul += str(start + 2)
        start += 2
        if i == precision-1:
            break
        calcul += ((i%2 == 0) and "-1" or "+1") + "/"
    print(calcul + "\n")
    return ("Result : " + str(eval((calcul + ")")))[:8])

print(sixDecimal(2950))