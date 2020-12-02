import pygame
from controller.game_listener import Game_Listener as gl
import view.Window as w
import time
from model.etat import Etat as Etat

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640
ACTORS_ICON_SIZE = 64
FR = 20

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
            cls.etat = Etat()
            cls.clock = pygame.time.Clock()
        return cls.__instance

    def run(self):
        number_of_tick = 0
        game_listener = gl()
        self.window.initialise_game(self.etat)
        while self.etat.loose is False and self.etat.win is False:
            self.window.update_icons(self.etat)
            self.etat.update_grid(number_of_tick, game_listener)
            self.clock.tick(FR)
            number_of_tick += 1
        self.window.update_icons(self.etat)
        time.sleep(3)
