import pygame as pg

class IconesActeurs:

    def __init__(self, ):
        self.sizeofIcon = size
        self.color = color
        self.coord1, self.coord2 = coord
        self.rect = pg.Rect(self.coord1,self.coord2, size, size)

    def getIcon(self):
        return self.color, self.rect

    def getAlive(self, act_fact):
        return act_fact.isAlive

    def setAlive(self, act_fact):
        act_fact.isAlive = False

    def isinCollision(self, window):
        return pg.sprite.spritecollide(self)