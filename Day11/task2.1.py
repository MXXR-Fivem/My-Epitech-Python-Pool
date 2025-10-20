import turtle

screen = turtle.Screen()
tlt = turtle.Turtle()
tlt.penup()
tlt.setpos(-50, -50)
tlt.pendown()
tlt.color("red")

for _ in range(4):
    tlt.forward(100)
    tlt.left(90)