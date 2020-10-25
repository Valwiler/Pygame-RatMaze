import pygame as pg

class IconesActeurs:

    def __init__(self, actor, size):
        self.sizeofIcon = size
        self.color = actor.color
        self.coord1, self.coord2 = actor.position
        self.rect = pg.Rect(self.coord1,self.coord2, self.sizeofIcon, self.sizeofIcon)

    def getIcon(self):
        return self.color, self.rect

    def getAlive(self, act_fact):
        return act_fact.isAlive

    def setAlive(self, act_fact):
        act_fact.isAlive = False

    def isinCollision(self, window):
        return pg.sprite.spritecollide(self)