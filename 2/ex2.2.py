import turtle

turtle.shape('turtle')

# черепашка рисует 0
def print_null():
    turtle.left(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(90)

# черепашка рисует 1
def print_one():
    turtle.left(90)
    turtle.forward(180)
    turtle.left(135)
    turtle.forward(126)
    turtle.left(135)

# черепашка рисует 2
def print_two():
    turtle.left(180)
    turtle.forward(90)
    turtle.right(135)
    turtle.forward(126)
    turtle.left(45)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(180)

# черепашка рисует 3
def print_three():
    turtle.penup()
    turtle.left(180)
    turtle.forward(90)
    turtle.pendown()
    turtle.right(135)
    turtle.forward(126)
    turtle.left(135)
    turtle.forward(90)
    turtle.right(135)
    turtle.forward(126)
    turtle.left(135)
    turtle.forward(90)
    turtle.left(180)

# черепашка рисует 4
def print_four():
    turtle.left(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.penup()
    turtle.forward(90)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)

# черепашка рисует 5
def print_five():
    turtle.left(180)
    turtle.forward(90)
    turtle.backward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(90)

# черепашка рисует 6
def print_six():
    turtle.left(180)
    turtle.forward(90)
    turtle.backward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.backward(90)
    turtle.left(135)
    turtle.forward(126)
    turtle.right(45)

# черепашка рисует 7
def print_seven():
    turtle.penup()
    turtle.left(180)
    turtle.forward(90)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(90)
    turtle.right(45)
    turtle.forward(126)
    turtle.left(135)
    turtle.forward(90)
    turtle.left(180)

# черепашка рисует 8
def print_eight():
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.backward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(90)

# черепашка рисует 9
def print_nine():
    turtle.backward(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.backward(90)
    turtle.right(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(90)
    turtle.left(90)

# Черепашка рисует нужную цифру
def print_numeral(n):
    turtle.penup()
    turtle.goto(iterator * 100, 0)
    turtle.pendown()
    if n == 0:
        print_null()
    elif n == 1:
        print_one()
    elif n == 2:
        print_two()
    elif n == 3:
        print_three()
    elif n == 4:
        print_four()
    elif n == 5:
        print_five()
    elif n == 6:
        print_six()
    elif n == 7:
        print_seven()
    elif n == 8:
        print_eight()
    else:
        print_nine()

postcode = str(input())
for iterator in range(len(postcode)):
    print_numeral(int(postcode[iterator]))
