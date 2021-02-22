import turtle

def circle(a, r):
    if a == 'l':
        for i in range(720):
            turtle.left(0.5)
            turtle.forward(r)
    else:
        for i in range(720):
            turtle.right(0.5)
            turtle.forward(r)

def arc(r):
    for i in range(90):
        turtle.left(2)
        turtle.forward(r)

turtle.shape('turtle')
turtle.penup()
turtle.goto(0, -114)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
circle('l' , 2)
turtle.end_fill()

turtle.penup()
turtle.goto(90, 160)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
circle('l' , 0.2)
turtle.end_fill()

turtle.left(180)

turtle.penup()
turtle.goto(-90, 160)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
circle('r' , 0.2)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.width(10)
turtle.color('black')
turtle.left(90)
turtle.begin_fill()
turtle.forward(20)
turtle.end_fill()

turtle.right(90)

turtle.penup()
turtle.goto(-90, 0)
turtle.pendown()
turtle.width(10)
turtle.color('red')
turtle.left(90)
arc(3.14)

input()