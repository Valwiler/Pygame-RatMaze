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
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        self.center = (width // 2, height // 2)

    def update_icons(self):

        self.ecran.fill(BLACK)
        for actor in self.actors:
            if isinstance(actor, a.Player):
                for other_object in self.actors:
                    if i.Actor_Icon(actor, self.actors_icons_size).is_in_collision(
                            i.Actor_Icon(other_object, self.actors_icons_size)):
                        if isinstance(other_object, a.Zombie):
                            self.end_game(actor, 'Défaite', RED)
                        elif isinstance(other_object, a.Fromage):
                            self.end_game(other_object, 'Victoire', WHITE)
            color, rect = i.Actor_Icon(actor, self.actors_icons_size).get_icon()
            pg.draw.rect(self.ecran, color, rect)
        pg.display.update()

    def end_game(self, actor_to_kill, message, screen_color):
        self.ecran.fill(screen_color)
        actor_to_kill.set_alive(False)
        self.game_over = True
        text = self.font.render(message, True, BLACK, screen_color)
        rect = text.get_rect()
        rect.center = self.center
        self.ecran.blit(text, rect)