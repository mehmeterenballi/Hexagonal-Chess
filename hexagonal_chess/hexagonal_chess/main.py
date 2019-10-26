import pygame as pg
import pawn
from Board import *


WIDTH, HEIGHT = 305, 315


def main():
    pg.init()

    allgroups = pg.sprite.LayeredUpdates()
    boardGroup = pg.sprite.Group()
    pawn_groups = pg.sprite.Group()

    screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)

    for i in range(0, 9):
        whitePawn = pawn.WhitePawn(pg.mouse.get_pos(), [30 * (i + 1), 290], allgroups, pawn_groups)

    for i in range(0, 10):
        WhitePawn = pawn.WhitePawn(pg.mouse.get_pos(), [(30 * (i + 1)) - 15, 260], allgroups, pawn_groups)

    for i in range(0, 9):
        blackPawn = pawn.BlackPawn(pg.mouse.get_pos(), [30 * (i + 1), 50], allgroups, pawn_groups)

    for i in range(0, 10):
        blackPawn = pawn.BlackPawn(pg.mouse.get_pos(), [(30 * (i + 1)) - 15, 20], allgroups, pawn_groups)

    gameboard = Board(allgroups, boardGroup)

    clock = pg.time.Clock()
    running = True

    while running:
        screen.fill((100, 100, 100))
        time = clock.tick()/1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        allgroups.update(time)
        allgroups.draw(screen)

        pg.display.flip()


if __name__ == "__main__":
    main()
