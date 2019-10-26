import pygame as pg
import pawn


class Board(pg.sprite.Sprite):

    def __init__(self, *groups):
        self._layer = 3
        self.groups = groups
        pg.sprite.Sprite.__init__(self, self.groups)

        self.image = self.board()
        self.imagecopy = self.image.copy()

        self.pos = [0, 0]
        self.rect = self.image.get_rect()

        self.rect.center = [self.pos[0] + self.rect.width / 2, self.pos[1] + self.rect.height / 2]

    def update(self, time):
        x, y = mouse = pg.mouse.get_pos()
        y = y - y % 30

        self.image = self.imagecopy.copy()
        if y % 60 == 0 and y < 300 and x < 300:
            x = x - x % 30
            self.image.blit(self.cell(0), (x, y))
            self.image.convert_alpha()

        if y % 60 == 30 and 15 < x < 270:
            x = x - (x + 15) % 30

            self.image.blit(self.cell(0), (x, y))
            self.image.convert_alpha()

    @staticmethod
    def cell(width=0):
        cell = pg.Surface((31, 41), pg.SRCALPHA, 32)
        pg.draw.polygon(cell, (1, 1, 1, 120), ((0, 10), (0, 30), (15, 40), (30, 30), (30, 10), (15, 0)), width)
        cell.set_colorkey((0, 0, 0))
        cell.convert()

        return cell

    @staticmethod
    def board():

        cell = Board.cell(1)

        surface = pg.Surface((305, 315), pg.SRCALPHA)

        for y in range(10):
            for x in range(10):
                if y % 2 == 0:
                    surface.blit(cell, (x * 30, y * 30))
                if y % 2 == 1 and x < 9:
                    surface.blit(cell, (x * 30 + 15, y * 30))

        surface.set_colorkey((0, 0, 0))
        surface.convert()

        return surface
