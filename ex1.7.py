import turtle

turtle.shape('turtle')

s = 0.01

for i in range(20):
    for j in range(45):
        turtle.forward(s)
        turtle.left(4)
        s += 0.01
