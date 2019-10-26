import pygame as pg

pg.init()


class Lists:
    whitePawns = []
    blackPawns = []
    possible_courses = []
    is_pos_courses_full = False


class WhitePawn(pg.sprite.Sprite):
    def __init__(self, mousePos, pos=[0, 0], *groups):
        self.groups = groups
        self._layer = 2
        pg.sprite.Sprite.__init__(self, self.groups)

        self.image = pg.image.load("pawns.png")
        self.image = self.image.subsurface((0, 0, 450, 580))
        self.image = pg.transform.scale(self.image, (15, 20))
        self.rect = self.image.get_rect()

        self.pos = pos.copy()
        self.rect.center = self.pos

        self.mousePos = mousePos
        self.is_chosen = False
        self.leftMouseButtonPressed = False

        self.possible_courses = [0, 0, 0, 0]

    def update(self, time):
        click = pg.mouse.get_pressed()
        self.mousePos = pg.mouse.get_pos()

        if not self.leftMouseButtonPressed:
            if self.rect.centerx + 15 > self.mousePos[0] > self.rect.centerx and \
                    self.rect.centery + 20 > self.mousePos[1] > self.rect.centery - 20:
                if click[0] == 1:
                    self.leftMouseButtonPressed = True
                    self.is_chosen = True

        if self.is_chosen:  # if self.leftMouseButtonPressed:
            self.possible_courses = [self.rect.centerx - 30, self.rect.centery - 30, self.rect.centerx + 30,
                                     self.rect.centery - 30]
            Lists.is_pos_courses_full = True
            Lists.possible_courses.append(self.possible_courses)
            if self.rect.centerx + 15 > self.possible_courses[0] > self.rect.centerx - 15 and \
                    self.rect.centery + 20 > self.possible_courses[1] > self.rect.centery - 20:
                if click[0] == 1:
                    self.rect.center = self.possible_courses[0], self.possible_courses[1]
                    self.leftMouseButtonPressed = False
                    self.is_chosen = False
                    Lists.is_pos_courses_full = False
                    Lists.possible_courses.clear()

            if self.rect.centerx + 15 > self.possible_courses[2] > self.rect.centerx - 15 and \
                    self.rect.centery + 20 > self.possible_courses[3] > self.rect.centery - 20:
                if click[0] == 1:
                    self.rect.center = self.possible_courses[2], self.possible_courses[3]
                    self.leftMouseButtonPressed = False
                    self.is_chosen = False
                    Lists.is_pos_courses_full = False
                    Lists.possible_courses.clear()


class BlackPawn(pg.sprite.Sprite):
    def __init__(self, mousePos: list, pos=[0, 0], *groups):
        self.groups = groups
        self._layer = 2
        pg.sprite.Sprite.__init__(self, self.groups)

        self.image = pg.image.load("pawns.png")
        self.image = self.image.subsurface(pg.Rect(450, 0, 450, 580))
        self.image = pg.transform.scale(self.image, (15, 20))
        self.rect = self.image.get_rect()

        self.pos = pos.copy()
        self.rect.center = self.pos

        self.mousePos = mousePos
        self.leftMouseButtonPressed = True

        self.radius = 5

    def update(self, time):
        click = pg.mouse.get_pressed()

        self.mousePos = pg.mouse.get_pos()

        self.rect.center = self.pos

        if self.rect.centerx - (15 / 2) < self.mousePos[0] < self.rect.centerx + (15 / 2) and \
                self.rect.centery + 10 > self.mousePos[1] > self.rect.centery - 10:
            if click[0] == 1:
                if not self.leftMouseButtonPressed:
                    self.leftMouseButtonPressed = True
                    if self.leftMouseButtonPressed:
                        self.pos[0] = self.mousePos[0] + self.mousePos[0] % 30 + self.rect.width / 2
                        self.pos[1] = self.mousePos[1] + self.mousePos[1] % 30 + self.rect.height / 2

            if self.leftMouseButtonPressed:
                for whitePawn in Lists.whitePawns:
                    if whitePawn.pos[0] - (15 / 2) < self.mousePos[0] < whitePawn.pos[0] + (15 / 2) and \
                            whitePawn.pos[1] - 10 < self.mousePos[1] < whitePawn.pos[1] + 10:
                        Lists.whitePawns.pop(Lists.whitePawns.index(whitePawn))
                        whitePawn.kill()
                self.leftMouseButtonPressed = False
