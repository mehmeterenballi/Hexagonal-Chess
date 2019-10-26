import pygame as pg
import random

WIDTH, HEIGHT = 600, 400

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

background = pg.Surface((WIDTH, HEIGHT))
background.fill((200, 200, 200))


def write(msg, size=10):
    font = pg.font.SysFont('none', size)
    text = font.render(msg, True, (0, 0, 0))
    text.convert()


write("mete")


class Hexagons(pg.sprite.Sprite):
    number = 0
    currentnumber = 0

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.groups)

        self.image = pg.Surface((35 + 1, 40 + 1))
        pg.draw.polygon(self.image, (1, 1, 1), ((0, 10), (0, 30), (17, 40), (35, 30), (35, 10), (17, 0)), 1)
        self.image.set_colorkey((0, 0, 0))
        self.image.convert()

        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.number = Hexagons.number
        Hexagons.number += 1
        self.occupied = False

    def update(self, time):
        mousepos = pg.mouse.get_pos()
        rectbool = (self.rect.left < mousepos[0] and self.rect.right - 1 > mousepos[0] and self.rect.top < mousepos[
            1] and self.rect.bottom > mousepos[1])
        self.smallrectbool = (self.rect.left < mousepos[0] and self.rect.right - 1 > mousepos[
            0] and self.rect.top + self.rect.width / 4 < mousepos[1] and self.rect.bottom - self.rect.width / 4 >
                              mousepos[1])
        upperleftbool = rectbool and not (
                    (mousepos[1] - self.rect.top - self.rect.width * 0.25) / (mousepos[0] - self.rect.left) > (
                        self.rect.height * 0.25 / self.rect.width * 0.5))
        upperrightbool = rectbool and not (
                    (mousepos[1] - self.rect.top - self.rect.width * 0.25) / (mousepos[0] - self.rect.right) > (
                        -self.rect.height * 0.25 / self.rect.width * 0.5))

        if self.smallrectbool:
            if pg.mouse.get_pressed()[2] and not self.occupied:
                self.occupied = True
                self.entity_number = Enemies(self).number


            elif pg.mouse.get_pressed()[0] and not self.occupied:
                for enemy in enemygroup.sprites():
                    if enemy.changeable:
                        self.occupied = True
                        enemy.boss.occupied = False
                        enemy.boss = self
                        enemy.rect.center = self.rect.center
                        enemy.changeable = False
                        self.__init__(self.rect.center)

            else:
                self.image = pg.Surface((35 + 1, 40 + 1))
                pg.draw.polygon(self.image, (1, 1, 1), ((0, 10), (0, 30), (17, 40), (35, 30), (35, 10), (17, 0)))
                self.image.set_colorkey((0, 0, 0))
                self.image.set_alpha(100)
                self.image.convert_alpha()


        else:
            self.image = pg.Surface((35 + 1, 40 + 1))
            pg.draw.polygon(self.image, (1, 1, 1), ((0, 10), (0, 30), (17, 40), (35, 30), (35, 10), (17, 0)), 1)
            self.image.set_colorkey((0, 0, 0))
            self.image.convert()


class Enemies(pg.sprite.Sprite):
    number = 0

    def __init__(self, boss):
        pg.sprite.Sprite.__init__(self, self.groups)

        self.boss = boss
        self.image = pg.Surface((35 + 1, 40 + 1))
        pg.draw.polygon(self.image, (200, 222, 0), (
        (0 + 2, 10 + 2), (0 + 2, 30 - 2), (17, 40 - 2), (35 - 2, 30 - 2), (35 - 2, 10 + 2), (17, 0 + 2)))
        self.image.set_colorkey((0, 0, 0))
        self.image.convert()

        self.rect = boss.rect
        self.number = Enemies.number
        Enemies.number += 1

        self.changeable = False

    def update(self, time):
        if pg.mouse.get_pressed()[0] and self.boss.smallrectbool:
            self.changeable = True


areagroup = pg.sprite.Group()
enemygroup = pg.sprite.Group()
allgroups = pg.sprite.Group()
Hexagons.groups = allgroups, areagroup
Enemies.groups = allgroups, enemygroup

"""
def area(a=4,b=10):
    for y in range(a,(a+b)//2-1):
            for x in range(int((WIDTH//34)/2)-y//2,int((WIDTH//34)/2)+y//2):
                if x==int((WIDTH//34)/2)+y//2-1 and y%2==0:
                    break

                if y%2==0:
                    x+=0.5

                Hexagons([x*34,y*40*0.75])


    for y in range((a+b)//2-1,b-1):
           y2=y
           y2=b+a-y2-2
           for x in range(int((WIDTH//34)/2)-y2//2,int((WIDTH//34)/2)+y2//2):
                if x==int((WIDTH//34)/2)+y2//2-1 and y%2==0:
                   break

                if y%2==0:
                    x+=0.5
                Hexagons([x*34,y*40*0.75])
"""

areawidth = WIDTH // 34


def area(x, y):
    for y in range(1, HEIGHT // int(40 * 0.75)):
        for x in range(1, areawidth):
            if y % 2 == 0:
                x += 0.5
            Hexagons((x * 34, y * 40 * 0.75))


area(6, 14)

clock = pg.time.Clock()
FPS = 60
running = True

screen.blit(background, (0, 0))

while running:
    time = clock.tick(FPS) / 1000.0
    # screen.blit(background,(0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    allgroups.clear(screen, background)
    allgroups.update(time)
    allgroups.draw(screen)

    pg.display.flip()

pg.quit()
