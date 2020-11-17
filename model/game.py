import pygame
import model.actor_factory as af
from controller.game_listener import Game_Listener as gl
import view.Window as w
import time
from model.etat import Etat as Etat

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640
ACTORS_ICON_SIZE = 64
FR = 1

NUMBER_OF_ACTORS = 5
LABORAT_ID = 0

COORDINATE_X = 0
COORDINATE_Y = 1


class Game:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Game, cls).__new__(cls)
            cls.window = w.Window(SCREEN_WIDTH, SCREEN_HEIGHT, ACTORS_ICON_SIZE)
            cls.Etat = Etat()
            # cls.running = True
            cls.clock = pygame.time.Clock()
        return cls.__instance

    def run(self):
        while self.Etat.loose is False and self.Etat.win is False:
            self.window.update_icons(self.Etat)
            self.Etat.update_grid()
            self.clock.tick(FR)
        #time.sleep(3)
    #
    #def position_validation(self, new_position):
    #    return (0 < new_position[COORDINATE_X] < SCREEN_WIDTH - ACTORS_ICON_SIZE) and \
    #           (0 < new_position[COORDINATE_Y] < SCREEN_HEIGHT - ACTORS_ICON_SIZE)
    #