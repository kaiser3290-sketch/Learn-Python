import turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.penup()
pen.goto(0,-60)
pen.setheading(90)
pen.pendown()
pen.color("white")
for a in range(1,6+1):
    pen.forward(100)
    pen.right(60)
pen.penup()
pen.left(90)
pen.forward(100)
pen.pendown()
for a in range(1,4+1):
    pen.forward(100)
    pen.right(90)
pen.penup()
pen.left(90)
pen.forward(150)
pen.pendown()
for a in range(1,3+1):
    pen.right(120)
    pen.forward(100)


turtle.done()