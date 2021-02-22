import turtle
from random import *

turtle.shape('turtle')
while True:
    if (randint(0, 101) % 2) == 0:
        turtle.forward(random()*10)
        turtle.left(180*random())
    else:
        turtle.forward(random()*10)
        turtle.right(180*random())




