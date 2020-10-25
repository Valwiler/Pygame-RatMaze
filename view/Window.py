import pygame as pg
import view.IconesActeur as i

import model.actor_factory as acf

class Window:

    def __init__(self, width, height):
        self.ecran = pg.display.set_mode((width, height))


    def update_icons(self, act_factory):
        self.ecran.fill((0, 0, 0))
        for icons in act_factory:
            color, rect = i.IconesActeurs(icons, 64).getIcon()
            pg.draw.rect(self.ecran, color, rect)
        pg.display.update()
