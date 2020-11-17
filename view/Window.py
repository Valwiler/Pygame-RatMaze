import pygame as pg
import view.IconesActeur as i
import model.actor as a
from model.etat import Etat as e

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE

class Window:

    def __init__(self, width, height, actors_icons_size, actors):
        self.ecran = pg.display.set_mode((width, height))
        self.actors = actors
        self.game_over = False
        self.actors_icons_size = actors_icons_size
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        self.center = (width // 2, height // 2)

    def update_icons(self):
        self.ecran.fill(BLACK)
        grid_etat = e.get_etat()
        couleur = { 0: (BLACK),
                    1: (GREY),
                    2: (BLUE),
                    3: (GREEN),
                    4: (YELLOW)
                }
        for i in range (len(grid_etat)):
            for j in range(len(grid_etat[i][j])):
                c = couleur.get(grid_etat[i][j])
                rect = pg.Rect(i*self.actors_icons_size, j * self.actors_icons_size,  self.actors_icons_size, self.actors_icons_size)
                pg.draw.rect(self.ecran, c, rect)
        pg.display.update()
        # self.ecran.fill(BLACK)
        # for actor in self.actors:
        #     if isinstance(actor, a.Player):
        #         for other_object in self.actors:
        #             if i.Actor_Icon(actor, self.actors_icons_size).is_in_collision(
        #                     i.Actor_Icon(other_object, self.actors_icons_size)):
        #                 if isinstance(other_object, a.Zombie):
        #                     self.end_game(actor, 'Défaite', RED)
        #                 elif isinstance(other_object, a.Fromage):
        #                     self.end_game(other_object, 'Victoire', WHITE)
        #     color, rect = i.Actor_Icon(actor, self.actors_icons_size).get_icon()
        #     pg.draw.rect(self.ecran, color, rect)
        # pg.display.update()

    def end_game(self, actor_to_kill, message, screen_color):
        self.ecran.fill(screen_color)
        actor_to_kill.set_alive(False)
        self.game_over = True
        text = self.font.render(message, True, BLACK, screen_color)
        rect = text.get_rect()
        rect.center = self.center
        self.ecran.blit(text, rect)