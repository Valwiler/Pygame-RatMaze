import pygame as pg
import view.IconesActeur as i
import model.actor as a

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Window:

    def __init__(self, width, height, actors_icons_size, actors):
        self.ecran = pg.display.set_mode((width, height))
        self.actors = actors
        self.game_over = False
        self.actors_icons_size = actors_icons_size
        self.background_color = BLACK
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        self.text1 = self.font.render('Victoire', True, BLACK, WHITE)
        self.text2 = self.font.render("Défaite", True, BLACK, RED)
        self.trect1 = self.text1.get_rect()
        self.trect2 = self.text2.get_rect()
        self.trect1.center = (width // 2, height // 2)
        self.trect2.center = (width // 2, height // 2)

    def update_icons(self):

        self.ecran.fill(self.background_color)
        for actor in self.actors:
            if isinstance(actor, a.Player):
                for other_object in self.actors:
                    if i.Actor_Icon(actor, self.actors_icons_size).is_in_collision(
                            i.Actor_Icon(other_object, self.actors_icons_size)):
                        if isinstance(other_object, a.Zombie):
                            self.background_color = RED
                            actor.set_alive(False)
                            self.game_over = True
                            self.ecran.blit(self.text2, self.trect2)
                            print('game over')
                        elif isinstance(other_object, a.Fromage):
                            self.background_color = WHITE
                            other_object.set_alive(False)
                            self.game_over = True
                            self.ecran.blit(self.text1, self.trect1)
                            print('Yay, you won !!!')
                        else:
                            pass
            color, rect = i.Actor_Icon(actor, self.actors_icons_size).get_icon()
            pg.draw.rect(self.ecran, color, rect)
        pg.display.update()
