import turtle

def ungle(n):
    turtle.left(90 + (360 / (2 * n)))
    for i in range(n):
        turtle.forward(10 + 7 * n)
        turtle.left(360 / n)
    turtle.right(360 / n)
    turtle.right(90 * (n - 2) / n)

turtle.shape('turtle')


for i in range(3, 11):
    turtle.penup()
    turtle.goto(7 * i, 0)
    turtle.pendown()
    ungle(i)


