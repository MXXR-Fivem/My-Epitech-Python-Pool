import turtle as t

t.speed(100)

t.pensize(0)
t.penup()
t.setpos(-15, -160)
t.pendown()
t.fillcolor("#fbbf2b")
t.begin_fill()
t.circle(125)
t.end_fill()

t.penup()
t.setpos(38, 0)
t.pensize(10)
t.pendown()

for i in range(35):
    t.pensize(10-(i*0.18))
    t.circle(i, 22.5)

t.penup()
t.setpos(-62, 0)
t.pensize(10)
t.pendown()

for i in range(35):
    t.pensize(10-(i*0.18))
    t.circle(-i, 22.5)

t.penup()
t.setpos(57.5, -90)
t.pendown()
t.pensize(6)
t.left(95)
t.circle(20, 80)
t.circle(-25, 80)
t.circle(20, 80)
t.circle(-25, 80)
t.circle(20, 80)

t.exitonclick()