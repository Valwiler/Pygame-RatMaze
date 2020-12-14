import model.actor as ac
import pygame as pg
from model.coord import Coord as coord, Coord

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = None


class Window:

    def __init__(self, width, height, actors_icons_size):
        self.ecran = pg.display.set_mode((width, height - actors_icons_size))
        self.actors_icons_size = actors_icons_size
        self.glass_pane = pg.Surface((width, height), flags=pg.SRCALPHA)
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        self.text1 = self.font.render('Gagné !', True, WHITE, BACKGROUND)
        self.text2 = self.font.render("Perdu !", True, BLACK, BACKGROUND)
        self.trect1 = self.text1.get_rect()
        self.trect2 = self.text2.get_rect()
        self.trect1.center = (width // 2, height // 2)
        self.trect2.center = (width // 2, height // 2)

    def initialise_game(self, etat):
        grid = etat.get_grid()

        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                actor = None
                plancher = None
                current_tile = etat.get_tile(coord(x, y))
                if len(current_tile.actors) > 1:
                    plancher = current_tile.get_actor(1)
                    actor = current_tile.get_actor(0)
                else:
                    plancher = current_tile.get_actor(0)
                image1 = plancher.get_sprite()
                self.ecran.blit(image1, (x * self.actors_icons_size, y * self.actors_icons_size))
                if actor is not None:
                    if isinstance(actor, ac.Cheese) or isinstance(actor, ac.Wall):
                        image2 = actor.get_sprite()
                        self.ecran.blit(image2, (x * self.actors_icons_size, y * self.actors_icons_size))
                    else:
                        image2 = actor.get_sprite()
                        self.glass_pane.blit(image2, (x * self.actors_icons_size, y * self.actors_icons_size))
                        self.ecran.blit(self.glass_pane, (0, 0))

    def update_icons(self, etat):

        changed_coords = etat.get_map_diff()

        for changed_coord in changed_coords:
            x, y = changed_coord[0], changed_coord[1]
            if len(etat.get_tile(Coord(x, y)).actors) > 1:
                plancher = etat.get_tile(Coord(x, y)).get_actor(1)
                img2 = plancher.get_sprite()
                self.glass_pane.blit(img2, (x * self.actors_icons_size, y * self.actors_icons_size))
            actor = etat.get_tile(Coord(x, y)).get_actor(0)
            img = actor.get_sprite()
            self.glass_pane.blit(img, (x * self.actors_icons_size, y * self.actors_icons_size))
            self.ecran.blit(self.glass_pane, (0, 0))
        if etat.loose is True:
            self.ecran.blit(self.text2, self.trect2)
        elif etat.win is True:
            self.ecran.blit(self.text1, self.trect1)

        pg.display.update()

