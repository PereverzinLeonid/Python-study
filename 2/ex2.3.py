import turtle

turtle.shape('turtle')
turtle.speed(50)
turtle.forward(400)
turtle.backward(800)
x = -400
y = 0

v_x = 5
v_y = 70
a_y = -10
a_x = 0
dt = 0

while True:
    if y >= 0:
        turtle.goto(x, y)

        v_x = v_x + a_x * dt
        v_y = v_y + a_y * dt

        x = x + v_x * dt
        y = y + v_y * dt

        dt += 0.0001
    else:
        v_y = - v_y
        dt += 0.0001
        turtle.goto(x, y)

        v_x = v_x + a_x * dt
        v_y = v_y + a_y * dt

        x = x + v_x * dt
        y = y + v_y * dt


