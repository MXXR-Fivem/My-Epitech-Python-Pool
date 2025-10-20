import turtle

def triangleSierpinski(lenght, level):
    if level == 1:
        for _ in range(3): # lowest
            tlt.fd(lenght)
            tlt.left(120)
    else:
        triangleSierpinski(lenght/2, level-1) # left
        tlt.fd(lenght/2)
        triangleSierpinski(lenght/2, level-1) # right
        tlt.bk(lenght/2)
        tlt.left(60)
        tlt.fd(lenght/2)
        tlt.right(60)
        triangleSierpinski(lenght/2, level-1) # top
        tlt.left(60)
        tlt.bk(lenght/2)
        tlt.right(60)

tlt = turtle.Turtle()
tlt.penup()
tlt.setpos(-150, -150)
tlt.pendown()
turtle.delay(0)
triangleSierpinski(500, 8)
turtle.exitonclick()