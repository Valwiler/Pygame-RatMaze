import pygame as pg


class Actor_Icon(pg.sprite.Sprite):

    def __init__(self, actor, size):
        pg.sprite.Sprite.__init__(self)
        self.sizeofIcon = size
        self.color = actor.color
        self.coord1, self.coord2 = actor.position
        self.rect = pg.Rect(self.coord1, self.coord2, self.sizeofIcon, self.sizeofIcon)

    def get_icon(self):
        return self.color, self.rect

    def get_alive(self, act_factory):
        return act_factory.isAlive

    def is_in_collision(self, other_object):
        return pg.sprite.collide_rect(self, other_object)
