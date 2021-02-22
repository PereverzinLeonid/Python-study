import turtle

def circle():
    for i in range(720):
        turtle.left(0.5)
        turtle.forward(1)

turtle.shape('turtle')

for i in range(6):
    circle()
    turtle.right(60)