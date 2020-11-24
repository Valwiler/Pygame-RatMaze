import pygame as pg
from model.coord import Coord as coord

#RED = (255, 0, 0)
#BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
#BLUE = pg.image.load("sprites/icone_rat.png")
#GREEN = pg.image.load("sprites/zombie.png")
#GREY = pg.image.load("sprites/mur_brique.png")
#YELLOW = pg.image.load("sprites/fromage.png")


class Window:

    def __init__(self, width, height, actors_icons_size):
        self.ecran = pg.display.set_mode((width, height-actors_icons_size))
        self.actors_icons_size = actors_icons_size

    def update_icons(self, etat):
        grid = etat.get_grid()
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                #if etat.get_tile(coord(x, y)).is_used() is True:
                    actor = etat.get_tile(coord(x, y)).get_actor()
                    img = actor.get_sprite()
                    self.ecran.blit(img, (x * self.actors_icons_size, y * self.actors_icons_size))



        pg.display.update()


                #if etat.win:
        #    self.background_color = WHITE
        #elif etat.loose:
        #    self.background_color = RED
        #self.ecran.fill(self.background_color)
        #couleur = {0: (self.background_color),
        #           1: (GREY),
        #           2: (BLUE),
        #           3: (GREEN),
        #           4: (YELLOW)
        #           }
        #for y, row in enumerate(grid):
        #    for x, col in enumerate(row):
        #        actor = etat.get_tile(coord(x, y)).get_actor()
        #        if not actor:
        #            c = couleur.get(0)
        #            img = pg.Rect(x * self.actors_icons_size, y * self.actors_icons_size, self.actors_icons_size,
        #                       self.actors_icons_size)
        #        else:
        #            c = couleur.get(actor.get_type())
        #            img = pg.transform.scale(c ,(self.actors_icons_size,self.actors_icons_size))
        #            img = img.get_rect()
        #        essai = pg.draw.rect(self.ecran, img)
        #        self.ecran.blit(essai, (x*self.actors_icons_size, y*self.actors_icons_size))
        #pg.display.update()

        #for y, row in enumerate(grid):
        #    for x, col in enumerate(row):
        #        actor = etat.get_tile(coord(x, y)).get_actor()
        #        if not actor:
        #            c = couleur.get(0)
        #        else:
        #            c = couleur.get(actor.get_type())
        #        rect = pg.Rect(x * self.actors_icons_size, y * self.actors_icons_size, self.actors_icons_size,
        #                       self.actors_icons_size)
        #        pg.draw.rect(self.ecran, c, rect)
        #pg.display.update()

