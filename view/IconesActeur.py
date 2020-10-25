import pygame
import pygame as pg
from pygame.sprite import Sprite


class IconesActeurs(pygame.sprite.Sprite):

    def __init__(self, actor, size):
        pygame.sprite.Sprite.__init__(self)
        self.sizeofIcon = size
        #self.sprite = Sprite([actor.position])
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
        print(pg.sprite.spritecollide(self))
        return pg.sprite.spritecollide(self)