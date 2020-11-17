import pygame as pg

import view
import view.IconesActeur as i
import model.actor as a
from model.etat import Etat as e
from model.coord import Coord as coord

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0,255,0)
GREY = (215,215,215)
YELLOW = (215,215,0)

class Window:

    def __init__(self, width, height, actors_icons_size):
        self.ecran = pg.display.set_mode((width, height))
        self.game_over = False
        self.actors_icons_size = actors_icons_size
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        self.center = (width // 2, height // 2)


    def update_icons(self, etat):
        grid = etat.get_grid()
        self.ecran.fill(BLACK)
        couleur = { 0: (BLACK),
                    1: (GREY),
                    2: (BLUE),
                    3: (GREEN),
                    4: (YELLOW)
                }
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                tile = etat.get_tile(coord(x,y))
                if not tile:
                    c = couleur.get(0)
                else:
                    c = couleur.get(tile.get_type())
                rect = pg.Rect(x*self.actors_icons_size, y * self.actors_icons_size,  self.actors_icons_size, self.actors_icons_size)
                pg.draw.rect(self.ecran, c, rect)
        pg.display.update()


    def end_game(self, actor_to_kill, message, screen_color):
        self.ecran.fill(screen_color)
        actor_to_kill.set_alive(False)
        self.game_over = True
        text = self.font.render(message, True, BLACK, screen_color)
        rect = text.get_rect()
        rect.center = self.center
        self.ecran.blit(text, rect)