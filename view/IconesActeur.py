import pygame
import pygame as pg
from pygame.sprite import Sprite


class IconesActeurs(pygame.sprite.Sprite):

    def __init__(self, actor, size):
        pygame.sprite.Sprite.__init__(self)
        self.sizeofIcon = size
        self.color = actor.color
        self.coord1, self.coord2 = actor.position
        self.rect = pg.Rect(self.coord1,self.coord2, self.sizeofIcon, self.sizeofIcon)

    def getIcon(self):
        return self.color, self.rect

    def getAlive(self, act_fact):
        return act_fact.isAlive

    def isinCollision(self, object):
        print(pg.sprite.collide_rect(self,object))
        return pg.sprite.collide_rect(self,object)