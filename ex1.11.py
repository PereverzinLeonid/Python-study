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

turtle.shape('turtle')

turtle.left(90)

r = 0.1

while True:
    circle("l", r)
    circle("r", r)
    r += 0.1