def sixDecimalV2(precision: int, start:int=3) -> tuple:
    calcul = "3+(1**2)/(6+(3**2)/(6"
    for i in range(precision):
        start += 2
        if i == precision-1:
            calcul += ("+(" + str(start) + "**2)/6") + (1+precision)*")"
            break
        calcul += ("+(" + str(start) + "**2)/(6")
    print(calcul + "\n")
    return ("Result : " + str(eval(calcul))[:8])

print(sixDecimalV2(50))