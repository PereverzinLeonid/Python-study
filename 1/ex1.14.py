import turtle

turtle.shape('turtle')

def star(n):
    if (n % 2) == 0:
        for i in range(n):
            turtle.forward(100)
            turtle.left(180 - 360 / n)
    else:
        for i in range(n):
            turtle.forward(100)
            turtle.left(180 - 180 / n)



n = int(input())

star(n)

input()