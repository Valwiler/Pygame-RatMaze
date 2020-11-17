import pygame as pg


class Actor_Icon():

    def __init__(self, actor, size):
        self.sizeofIcon = size
        self.color = actor.type
        self.coord1, self.coord2 = actor.position
        self.rect = pg.Rect(self.coord1, self.coord2, self.sizeofIcon, self.sizeofIcon)

    def get_icon(self):
        return self.color, self.rect
    ##############
    # DEPRECATED #
    ##############
    def is_in_collision(self, other_object):
        return pg.sprite.collide_rect(self, other_object)
