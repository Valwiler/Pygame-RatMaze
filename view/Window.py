import pygame as pg
from model.coord import Coord as coord


class Window:

    def __init__(self, width, height, actors_icons_size):
        self.ecran = pg.display.set_mode((width, height - actors_icons_size))
        self.actors_icons_size = actors_icons_size
        self.glass_pane = pg.Surface((width, height))

    def initialise_game(self, etat):
        grid = etat.get_grid()
        actor = None
        plancher = None
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                current_tile = etat.get_tile(coord(x, y))
                if len(current_tile.actors) > 1:
                    plancher = current_tile.get_actor(1)
                    actor = current_tile.get_actor(0)
                else:
                    plancher = current_tile.get_actor(0)
                image1 = plancher.get_sprite()
                self.ecran.blit(image1, (x * self.actors_icons_size, y * self.actors_icons_size))
                if actor is not None:
                    image2 = actor.get_sprite()
                    self.glass_pane.blit(image2, (x * self.actors_icons_size, y * self.actors_icons_size))


    def update_icons(self, etat):
        tiles_changed = etat.get_map_diff()
        self.glass_pane.
        for tile in tiles_changed:
            x, y = tile.get_coordinate()

            # if etat.get_tile(coord(x, y)).is_used() is True:
            actor = tile.get_actor(0)
            img = actor.get_sprite()
            self.glass_pane.blit(img, (x * self.actors_icons_size, y * self.actors_icons_size))

        pg.display.update()
