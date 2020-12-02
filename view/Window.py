import pygame as pg
from model.coord import Coord as coord


class Window:

    def __init__(self, width, height, actors_icons_size):
        self.ecran = pg.display.set_mode((width, height - actors_icons_size))
        self.actors_icons_size = actors_icons_size

    def initialise_game(self, etat):
        grid = etat.get_grid()
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                current_tile = etat.get_tile(coord(x, y))
                actor_selector = 1 if len(current_tile.actors) > 1 else 0
                actor = current_tile.get_actor(actor_selector)
                image = actor.get_sprite()
                self.ecran.blit(image, (x * self.actors_icons_size, y * self.actors_icons_size))

    def update_icons(self, etat):
        grid = etat.get_grid()
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                # if etat.get_tile(coord(x, y)).is_used() is True:
                actor = etat.get_tile(coord(x, y)).get_actor(0)
                img = actor.get_sprite()
                self.ecran.blit(img, (x * self.actors_icons_size, y * self.actors_icons_size))

        pg.display.update()
