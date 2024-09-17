import turtle
t = turtle.Turtle()
s = turtle.Screen()
t.shapesize(0.2, 0.2)
t.speed(0)
s.bgcolor("black")
t.fillcolor("white")
t.begin_fill()

t.left(50)
t.forward(240)
t.circle(90, 200)
t.left(221)
t.circle(90, 200)
t.forward(260)

t.end_fill()

turtle.done()