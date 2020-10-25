import pygame as pg
import view.IconesActeur as i
import model.actor_factory as acf

class Window:

    def __init__(self):
        w, h = 1024, 640
        ecran = pg.display.set_mode((w, h))


    def update_icons(self, act_factory):
        for icons in act_factory:
            pg.draw.rect(self.ecran, acf.Actor_Factory.getActor[icons]  )