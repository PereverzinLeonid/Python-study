import turtle

def arc(r):
        for i in range(90):
            turtle.left(2)
            turtle.forward(r)

turtle.shape('turtle')

turtle.left(90)
turtle.penup()
turtle.goto(300, 0)
turtle.pendown()

while True:
    arc(2)
    arc(0.5)