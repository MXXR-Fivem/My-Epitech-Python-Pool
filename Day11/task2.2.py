import turtle

toto = turtle.Screen()
toto.bgcolor("black")
titi = turtle.Turtle()
titi.color("red")

for i in range(3):
    titi.right(90)
    titi.circle(42)
toto.exitonclick()

# draw 3 circles in red with black background and exit on click