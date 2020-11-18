import pygame as pg
from model.coord import Coord as coord

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GREY = (215, 215, 215)
YELLOW = (215, 215, 0)


class Window:

    def __init__(self, width, height, actors_icons_size):
        self.ecran = pg.display.set_mode((width, height-actors_icons_size))
        self.background_color = BLACK
        self.actors_icons_size = actors_icons_size

    def update_icons(self, etat):
        grid = etat.get_grid()
        if etat.win:
            self.background_color = WHITE
        elif etat.loose:
            self.background_color = RED
        self.ecran.fill(self.background_color)
        couleur = {0: (self.background_color),
                   1: (GREY),
                   2: (BLUE),
                   3: (GREEN),
                   4: (YELLOW)
                   }
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                actor = etat.get_tile(coord(x, y)).get_actor()
                if not actor:
                    c = couleur.get(0)
                else:
                    c = couleur.get(actor.get_type())
                rect = pg.Rect(x * self.actors_icons_size, y * self.actors_icons_size, self.actors_icons_size,
                               self.actors_icons_size)
                pg.draw.rect(self.ecran, c, rect)
        pg.display.update()

