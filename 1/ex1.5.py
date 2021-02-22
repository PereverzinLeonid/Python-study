import turtle

turtle.shape('turtle')

for i in range(0, 100, 10):
    turtle.penup()
    turtle.goto(i, -i)
    turtle.pendown()
    for j in range(4):
        turtle.left(90)
        turtle.forward(50 + 2 * i)

input()