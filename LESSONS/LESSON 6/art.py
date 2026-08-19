import turtle
screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.penup()
pen.goto(0,0)
pen.setheading(90)
pen.pendown()
pen.speed("fastest")
pen.color("white")
for p in range(1,100):
    pen.forward(2*p)
    pen.right(91)

pen.penup()
pen.goto(0,-60)
pen.setheading(90)
pen.pendown()
pen.color("yellow","aqua")
pen.begin_fill()
for a in range(1,5+1):
    pen.forward(100)
    pen.right(144)
pen.end_fill()

turtle.done()