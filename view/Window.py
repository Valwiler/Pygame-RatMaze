from operator import mod
import model.actor as ac
from model import etat as et
import pygame as pg
from model.coord import Coord as coord, Coord


# todo gestion des sprites et correction de syntaxe (if else imbrique)

class Window:

    def __init__(self, width, height, actors_icons_size):
        self.ecran = pg.display.set_mode((width, height - actors_icons_size))
        self.actors_icons_size = actors_icons_size
        self.glass_pane = pg.Surface((width, height), flags=pg.SRCALPHA)

    def initialise_game(self, etat):
        grid = etat.get_grid()

        # image1, image2 = None
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
                #print(str(current_tile.get_actor(0).get_type()))
                image1 = plancher.get_sprite()
                self.ecran.blit(image1, (x * self.actors_icons_size, y * self.actors_icons_size))
                if actor is not None:
                    if isinstance(actor, ac.Cheese) or isinstance(actor, ac.Wall) :
                        image2 = actor.get_sprite()
                        self.ecran.blit(image2, (x * self.actors_icons_size, y * self.actors_icons_size))
                    else:
                        image2 = actor.get_sprite()
                        self.glass_pane.blit(image2, (x * self.actors_icons_size, y * self.actors_icons_size))
                        self.ecran.blit(self.glass_pane, (0, 0))

    def update_icons(self, etat):

        changed_coords = etat.get_map_diff()

        for changed_coord in changed_coords:
            # x, y = changed_coord.get_x(), changed_coord.get_y()
            x, y = changed_coord[0], changed_coord[1]
            actor = etat.get_tile(Coord(x,y)).get_actor(0)
            img = actor.get_sprite()
            self.glass_pane.blit(img, (x * self.actors_icons_size, y * self.actors_icons_size))
            self.ecran.blit(self.glass_pane, (0, 0))

        etat.clear_map_diff()
        pg.display.update()
