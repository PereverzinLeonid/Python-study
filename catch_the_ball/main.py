import pygame
import numpy as np
from pygame.draw import *
from random import randint

# файл таблицы игроков
name = input()
top = open('Top_players.txt', 'w')

pygame.init()
FPS = 60

# создание фона
width = 1200
height = 800
screen = pygame.display.set_mode((width, height))
screen.fill((0, 0, 0))

# создание множеества цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

# класс обычного шарика - двигается очень предсказуемо, но почти п любой момент может помереть
class usually_ball():
    x_cordinant = 0
    y_cordinant = 0
    radius = 0
    color = 0
    x_velocity = 0
    y_velocity = 0
    time = 0
    time_life = 0

# класс необычного шарика - безграничная жизнь, но двигается непонятно как
class unusually_ball():
    x_cordinant = 0
    y_cordinant = 0
    x_velocity = 0
    y_velocity = 0
    radius = 0
    color = 0

# начальные параметры: ограничистели скоростей, время жизни обычных шариков и ограничители на радиусы
min_velocity = 1
max_velocity = 3
min_time_life = 100
max_time_life = 200
min_radius = 10
max_radius = 100

# массив обчычных шариков
count_usually_ball = 10
data_usually_ball = []

# массив необычных шариков
count_unusually_ball = 5
data_unusually_ball = []

# очки человека, набранные в игре
score = 0
def text(score):
    f1 = pygame.font.SysFont(None, 55)
    text = f1.render(score, 1, BLUE)
    screen.blit(text, (60, 20))

# создание обычного шарика
def new_usually_ball(i):
    data_usually_ball.append(usually_ball())
    data_usually_ball[i].x_cordinant = randint(int(width * 0.1), int(width * 0.9))
    data_usually_ball[i].y_cordinant = randint(int(width * 0.1), int(height * 0.9))
    data_usually_ball[i].x_velocity = randint(-max_velocity, max_velocity)
    data_usually_ball[i].y_velocity = randint(-max_velocity, max_velocity)
    data_usually_ball[i].radius = randint(min_radius, max_radius)
    data_usually_ball[i].color = COLORS[randint(0, 5)]
    data_usually_ball[i].time = 0
    data_usually_ball[i].time_life = randint(min_time_life, max_time_life)

# создание необычного шарика
def new_unusually_ball(i):
    data_unusually_ball.append(unusually_ball())
    data_unusually_ball[i].x_cordinant = randint(int(width * 0.1), int(width * 0.9))
    data_unusually_ball[i].y_cordinant = randint(int(width * 0.1), int(height * 0.9))
    data_unusually_ball[i].x_velocity = randint(-max_velocity, max_velocity)
    data_unusually_ball[i].y_velocity = randint(-max_velocity, max_velocity)
    data_unusually_ball[i].radius = randint(min_radius, max_radius)
    data_unusually_ball[i].color = COLORS[randint(0, 5)]

# заполняю массив обычными шариками
for i in range(count_usually_ball):
    new_usually_ball(i)

# заполняю массив необычными шариками
for i in range(count_unusually_ball):
    new_unusually_ball(i)

# начало отрисовки
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            output = "Player score = " + str(score) + " - " + name + "\n"
            top.write(output) # вывод таблицы игроков
            finished = True
        # проверка попадания игрока по шарику
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i in range(count_usually_ball):
                if (mouse_pos[0] - data_usually_ball[i].x_cordinant) ** 2 + (mouse_pos[1] - data_usually_ball[i].y_cordinant) ** 2 <= data_usually_ball[i].radius ** 2:
                    new_usually_ball(i)
                    score = score + 1
            for i in range(count_unusually_ball):
                if (mouse_pos[0] - data_unusually_ball[i].x_cordinant) ** 2 + (mouse_pos[1] - data_unusually_ball[i].y_cordinant) ** 2 <= data_unusually_ball[i].radius ** 2:
                    new_unusually_ball(i)
                    score = score + 3


    # работа с обычным шариком
    for i in range(count_usually_ball):
        circle(screen, data_usually_ball[i].color, (data_usually_ball[i].x_cordinant, data_usually_ball[i].y_cordinant), data_usually_ball[i].radius)
        data_usually_ball[i].time += 1
        if data_usually_ball[i].time >= data_usually_ball[i].time_life:
            new_usually_ball(i)

        # проверяем шарика из зоны экрана

        if data_usually_ball[i].x_cordinant > width - data_usually_ball[i].radius:
            data_usually_ball[i].x_velocity = randint(-max_velocity, 0)
        if data_usually_ball[i].x_cordinant < data_usually_ball[i].radius:
            data_usually_ball[i].x_velocity = randint(0, max_velocity)
        if data_usually_ball[i].y_cordinant > height - data_usually_ball[i].radius:
            data_usually_ball[i].y_velocity = randint(-max_velocity, 0)
        if data_usually_ball[i].y_cordinant < data_usually_ball[i].radius:
            data_usually_ball[i].y_velocity = randint(0, max_velocity)

        # изменяем положение обычного шарика

        data_usually_ball[i].x_cordinant = data_usually_ball[i].x_cordinant + data_usually_ball[i].x_velocity
        data_usually_ball[i].y_cordinant = data_usually_ball[i].y_cordinant + data_usually_ball[i].y_velocity

    # работа с необычным шариком
    for i in range(count_unusually_ball):
        circle(screen, data_unusually_ball[i].color, (data_unusually_ball[i].x_cordinant, data_unusually_ball[i].y_cordinant), data_unusually_ball[i].radius)

        # проверяем выход шарика из зоны экрана

        if data_unusually_ball[i].x_cordinant > width - data_unusually_ball[i].radius:
            data_unusually_ball[i].x_velocity = randint(-max_velocity, 0)
        if data_unusually_ball[i].x_cordinant < data_unusually_ball[i].radius:
            data_unusually_ball[i].x_velocity = randint(0, max_velocity)
        if data_unusually_ball[i].y_cordinant > height - data_unusually_ball[i].radius:
            data_unusually_ball[i].y_velocity = randint(-max_velocity, 0)
        if data_unusually_ball[i].y_cordinant < data_unusually_ball[i].radius:
            data_unusually_ball[i].y_velocity = randint(0, max_velocity)

        # изменяем скорость необычного шарика

        data_unusually_ball[i].x_velocity = data_unusually_ball[i].x_velocity + randint(-max_velocity, max_velocity)
        data_unusually_ball[i].y_velocity = data_unusually_ball[i].y_velocity + randint(-max_velocity, max_velocity)

        # изменяем положение необычного шарика

        data_unusually_ball[i].x_cordinant = data_unusually_ball[i].x_cordinant + data_unusually_ball[i].x_velocity
        data_unusually_ball[i].y_cordinant = data_unusually_ball[i].y_cordinant + data_unusually_ball[i].y_velocity

    text(str(score))
    pygame.display.update()
    screen.fill((0, 0, 0))

pygame.quit()