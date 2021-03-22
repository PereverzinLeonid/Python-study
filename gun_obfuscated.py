import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
pi = 3.14

# рисует мухомор
def mushroom(x0, y0, length, width):

    ellipse(screen, (249, 255, 255),
            (x0 + 0.13 * length, y0 + 0.52 * width, 0.05 * length, 0.2 * width))
    ellipse(screen, 'black', (x0 + 0.13 * length, y0 + 0.52 * width, 0.05 * length, 0.2 * width), 1)
    ellipse(screen, (228, 13, 31),
            (x0 + 0.08 * length, y0 + 0.5 * width, 0.15 * length, 0.1 * width))
    ellipse(screen, 'black', (x0 + 0.08 * length, y0 + 0.5 * width, 0.15 * length, 0.1 * width), 1)
    circle(screen, (249, 255, 255), (x0 + 0.13 * length, y0 + 0.52 * width), 0.005 * length)
    circle(screen, (249, 255, 255), (x0 + 0.16 * length, y0 + 0.55 * width), 0.007 * length)
    circle(screen, (249, 255, 255), (x0 + 0.17 * length, y0 + 0.52 * width), 0.009 * length)

    circle(screen, (249, 255, 255), (x0 + 0.11 * length, y0 + 0.56 * width), 0.006 * length)
    circle(screen, (249, 255, 255), (x0 + 0.12 * length, y0 + 0.58 * width), 0.008 * length)

# рисует лужу
def ej(x0, y0, length, width):
    ellipse(screen, (253, 198, 105),
            (x0 + 0.88 * length, y0 + 0.25 * width, 0.07 * length, 0.04 * width))  # leg
    ellipse(screen, 'black', (x0 + 0.88 * length, y0 + 0.25 * width, 0.07 * length, 0.04 * width), 1)
    ellipse(screen, (253, 198, 105),
            (x0 + 0.52 * length, y0 + 0.13 * width, 0.4 * length, 0.2 * width))  # body
    ellipse(screen, 'black', (x0 + 0.52 * length, y0 + 0.13 * width, 0.4 * length, 0.2 * width), 1)
    ellipse(screen, (253, 198, 105),
            (x0 + 0.85 * length, y0 + 0.3 * width, 0.08 * length, 0.05 * width))  # leg
    ellipse(screen, 'black', (x0 + 0.85 * length, y0 + 0.3 * width, 0.08 * length, 0.05 * width), 1)

    ellipse(screen, (253, 198, 105),
            (x0 + 0.85 * length, y0 + 0.3 * width, 0.08 * length, 0.05 * width))  # head
    ellipse(screen, 'black', (x0 + 0.85 * length, y0 + 0.3 * width, 0.08 * length, 0.05 * width), 1)

# рисует дерево
def tree(x0, y0, width, length):

    rect(screen, (173, 76, 43), (x0, y0, width, length))
    rect(screen, (104, 52, 36), (x0 + 0.05*width, y0, 0.05*width, 1*length))
    rect(screen, (104, 52, 36), (x0 + 0.15 * width, y0, 0.03 * width, 1 * length))
    rect(screen, (104, 52, 36), (x0 + 0.2 * width, y0, 0.03 * width, 1 * length))
    rect(screen, (104, 52, 36), (x0 + 0.3 * width, y0, 0.07 * width, 1 * length))

    rect(screen, (104, 52, 36), (x0 + 0.4 * width, y0, 0.7 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.45 * width, y0, 0.05 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.6 * width, y0, 0.07 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.7 * width, y0, 0.02 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.8 * width, y0, 0.02 * width, 1 * length))
    rect(screen, (63, 26, 13), (x0 + 0.9 * width, y0, 0.15 * width, 1 * length))

# рисует фон
def backfround():
    rect(screen, (66, 92, 35), (0, 0, 600, 500))
    rect(screen, (150, 120, 68), (0, 500, 600, 300))
# рисует часть животного (тело)
def Body(screen, x, y, zoom, color_body):
    ellipse(screen, color_body, (x - 68 * zoom, y - 32 * zoom, 140 * zoom, 64 * zoom))
    ellipse(screen, color_body, (x + 38 * zoom, y - 120 * zoom, 40 * zoom, 105 * zoom))
    ellipse(screen, color_body, (x + 43 * zoom, y - 140 * zoom, 50 * zoom, 32 * zoom))
# рисует часть животного (глаза)
def Eyes(screen: pygame.display, x, y, zoom, color_body, color_eye_1, color_eye_2):
    ellipse(screen, color_eye_2, (x + 52 * zoom, y - 138 * zoom, 24 * zoom, 20 * zoom))
    ellipse(screen, color_eye_1, (x + 65 * zoom, y - 133 * zoom, 10 * zoom, 8 * zoom))
    glasik = pygame.Surface((12 * zoom, 6 * zoom), pygame.SRCALPHA)
    ellipse(glasik, color_body, (0, 0, 11 * zoom, 11 * zoom))
    glasik_rot = pygame.transform.rotate(glasik, -30)
    screen.blit(glasik_rot, (x + 58 * zoom, y - 138 * zoom))

# рисует часть животного (ноги)
def Legs(screen, x, y, zoom, color_body):
    ellipse(screen, color_body, (x - 10 * zoom, y + 20 * zoom, 20 * zoom, 48 * zoom))
    ellipse(screen, color_body, (x - 10 * zoom, y - 25 * zoom, 20 * zoom, 50 * zoom))
    ellipse(screen, color_body, (x -  5 * zoom, y + 65 * zoom, 20 * zoom, 15 * zoom))
# рисует часть животного (рога)
def Horns(screen, x, y, zoom, color_body):
    polygon(screen, color_body, [(x, y), (x - 10 * zoom, y - 10 * zoom), (x - 15 * zoom, y - 20 * zoom), (x - 18 * zoom, y - 30 * zoom), (x - 10 * zoom, y - 20 * zoom), (x, y - 10 * zoom), (x + 5 * zoom, y - 11 * zoom)])
    polygon(screen, color_body, [(x + 14 * zoom, y - 4 * zoom), (x + 4 * zoom, y - 14 * zoom), (x - 1 * zoom, y - 24 * zoom), (x - 4 * zoom, y - 34 * zoom), (x + 4 * zoom, y - 24 * zoom), (x + 14 * zoom, y - 14 * zoom), (x + 19 * zoom, y - 4 * zoom)])
# рисует животное
def beee(screen, x, y, zoom, color_body, color_eye_1, color_eye_2):
    Body(screen, x, y, zoom, color_body)
    Eyes(screen, x, y, zoom, color_body, color_eye_1, color_eye_2)
    Horns(screen, x + 50 * zoom, y - 130 * zoom, zoom / 1.5, color_body)
    Legs(screen, x + 45 * zoom, y + 38 * zoom, zoom, color_body)
    Legs(screen, x - 25 * zoom, y + 38 * zoom, zoom, color_body)
    Legs(screen, x - 51 * zoom, y + 13 * zoom, zoom, color_body)
    Legs(screen, x + 23 * zoom, y + 13 * zoom, zoom, color_body)

backfround()
# everything else
mushroom(150, 420, 600, 400)
tree(80, 0, 120, 790)
tree(0, 0, 50, 520)
tree(500, 0, 40, 520)
tree(565, 0, 30, 540)
mushroom(250, 360, 350, 200)
mushroom(0, 430, 600, 500)
beee(screen, 400, 500, 0.8, (255, 248, 220), (0, 0, 0), (128, 0, 0))


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()