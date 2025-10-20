import turtle

screen = turtle.Screen()

def draw_polygon(sides: int, size: int=100) -> None:
    if not (2 < sides < 10) or not isinstance(sides, int):
        raise ValueError
    tlt = turtle.Turtle()
    tlt.penup()
    tlt.setpos(-50, -50)
    tlt.pendown()
    angles = [120, 90, 72.5, 60, 51.5, 45, 40]
    for _ in range(sides):
        tlt.forward(size)
        tlt.left(angles[sides-3])

draw_polygon(9, 125)