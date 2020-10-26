import pygame
import model.actor_factory as af
import controller.game_listener as gl
import view.Window as w
import time

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640
ACTORS_ICON_SIZE = 64
MVT = 1
FR = 300

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

    def run(self):
        while self.running and self.window.game_over is False:
            self.action_interpreter()
            self.window.update_icons()
            self.clock.tick(FR)

        time.sleep(1)

    def position_validation(self, new_position):
        return (0 < new_position[COORDINATE_X] < SCREEN_WIDTH - ACTORS_ICON_SIZE) and \
               (0 < new_position[COORDINATE_Y] < SCREEN_HEIGHT - ACTORS_ICON_SIZE)

    def action_interpreter(self):
        pressed_up, pressed_down, pressed_left, pressed_right = self.game_listener.get_input()
        new_position = [self.player.position[COORDINATE_X], self.player.position[COORDINATE_Y]]
        if pressed_left:
            new_position[COORDINATE_X] -= MVT
        if pressed_right:
            new_position[COORDINATE_X] += MVT
        if pressed_up:
            new_position[COORDINATE_Y] -= MVT
        if pressed_down:
            new_position[COORDINATE_Y] += MVT

        if self.position_validation(new_position):
            self.player.set_position(new_position)

