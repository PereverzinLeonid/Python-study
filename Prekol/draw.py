import pygame

from pygame.draw import *

pygame.init()
# фон
def background():
    # небо
    rect(sc, (166, 241, 160), (0, 350, 1500, 1500))
    # земля
    rect(sc, (138, 170, 232), (0, 0, 1500, 350))
# чел 1
def left_man():
    line(sc, BLACK, [250, 520], [240, 620])
    line(sc, BLACK, [270, 520], [280, 620])
    line(sc, BLACK, [220, 620], [240, 620])
    line(sc, BLACK, [300, 620], [280, 620])
    ellipse(screen, (192, 126, 187), (207, 325, 107, 200))
    circle(sc, (200, 200, 200), (260, 290), 40)
    line(sc, BLACK, [410, 420], [290, 340])
    line(sc, BLACK, [110, 420], [230, 340])
# чел 4
def right_man():
    line(sc, BLACK, [1140, 520], [1120, 620])
    line(sc, BLACK, [1160, 520], [1180, 620])
    line(sc, BLACK, [1100, 620], [1120, 620])
    line(sc, BLACK, [1200, 620], [1180, 620])
    ellipse(screen, (192, 126, 187), (1096, 325, 107, 200))
    circle(sc,(200,200,200),(1150,290),40)
    line(sc, BLACK, [1300, 420], [1180, 340])
    line(sc, BLACK, [990, 420], [1120, 340])
# чел 2
def left_woman():
    line(sc, BLACK, [520, 520], [500, 620])
    line(sc, BLACK, [580, 520], [600, 620])
    line(sc, BLACK, [500, 620], [480, 620])
    line(sc, BLACK, [600, 620], [620, 620])
    polygon(sc, (255, 0, 255), [(550, 320), (500, 520), (600, 520)])
    circle(sc, (200, 200, 200), (550, 290), 40)
    line(sc, BLACK, [410, 420], [545, 340])
    line(sc, BLACK, [695, 340], [615, 380])
    line(sc, BLACK, [615, 380], [555, 340])
# чел 3
def right_woman():
    line(sc, BLACK, [820, 520], [800, 620])
    line(sc, BLACK, [880, 520], [900, 620])
    line(sc, BLACK, [920, 620], [900, 620])
    line(sc, BLACK, [780, 620], [800, 620])
    polygon(sc, (255, 0, 255), [(850, 320), (800, 520), (900, 520)])
    circle(sc, (200, 200, 200), (850, 290), 40)
    line(sc, BLACK, [990, 420], [855, 340])
    line(sc, BLACK, [695, 340], [775, 380])
    line(sc, BLACK, [775, 380], [845, 340])
# сердце
def heart():
    triangle2 = [(100, 320), (150, 250), (60, 240)]
    polygon(sc, (250, 0, 0), triangle2)
    circle(sc, (250, 0, 0), (84, 235), 23)
    circle(sc, (250, 0, 0), (128, 239), 23)
    line(sc, BLACK, [100, 320], [110, 420])
# морожка
def ice_cream_2():
    triangle3 = [(1300, 415), (1335, 330), (1285, 330)]
    polygon(sc, (255, 255, 0), triangle3)
    circle(sc, (0, 0, 255), (1327, 330), 17)
    circle(sc, (255, 255, 255), (1295, 330), 17)
    circle(sc, (128, 0, 0), (1303, 315), 17)
# морожка шарик
def ice_cream_1():
    triangle3 = [(650, 250), (670, 180), (620, 180)]
    polygon(sc, (255, 255, 0), triangle3)
    circle(sc, (255, 0, 0), (662, 180), 17)
    circle(sc, (255, 255, 255), (630, 180), 17)
    circle(sc, (128, 0, 0), (638, 165), 17)
    line(sc, (128, 0, 0), [650, 250], [695, 340])


FPS = 10
screen = pygame.display.set_mode((1500, 1500))

BLACK = (0, 0, 0)
sc = screen

background()
left_man()
left_woman()
right_woman()
right_man()
ice_cream_1()
ice_cream_2()
heart()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()