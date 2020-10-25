import pygame
import model.actor_factory as af
import controller.game_listener as gl
import view.Window as w
import time

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640
ACTORS_ICON_SIZE = 64
MVT = 10
FR = 30

NUMBER_OF_ACTORS = 5
LABORAT_ID = 0

COORDINATE_X = 0
COORDINATE_Y = 1

class Game:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Game, cls).__new__(cls)
            cls.actor_factory = af.Actor_Factory(NUMBER_OF_ACTORS)
            cls.player = cls.actor_factory.get_actor(LABORAT_ID)
            cls.window = w.Window(SCREEN_WIDTH, SCREEN_HEIGHT, ACTORS_ICON_SIZE, cls.actor_factory.get_actors())
            cls.game_listener = gl.Game_Listener()
            cls.running = True
            cls.clock = pygame.time.Clock()
        return cls.__instance

    def new_position_validation(self):

        if self.player.position[COORDINATE_X] < 0:
            self.player.position[COORDINATE_X] = 0
        elif self.player.position[COORDINATE_X] > SCREEN_WIDTH - ACTORS_ICON_SIZE:
            self.player.position[COORDINATE_X] = SCREEN_WIDTH - ACTORS_ICON_SIZE
        elif self.player.position[COORDINATE_Y] < 0:
            self.player.position[COORDINATE_Y] = 0
        elif self.player.position[COORDINATE_Y] > SCREEN_HEIGHT - ACTORS_ICON_SIZE:
            self.player.position[COORDINATE_Y] = SCREEN_HEIGHT - ACTORS_ICON_SIZE

    def run(self):
        while self.running and self.window.game_over is False:
            pressed_up, pressed_down, pressed_left, pressed_right = self.game_listener.get_input()
            if pressed_left:
                self.player.position[COORDINATE_X] -= MVT
            if pressed_right:
                self.player.position[COORDINATE_X] += MVT
            if pressed_up:
                self.player.position[COORDINATE_Y] -= MVT
            if pressed_down:
                self.player.position[COORDINATE_Y] += MVT
            self.window.update_icons()
            self.clock.tick(FR)
            self.new_position_validation()

        self.window.update_icons()
        time.sleep(2)
