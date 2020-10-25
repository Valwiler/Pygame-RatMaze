import pygame
import model.actor_factory as af
import controller.game_listener as gl
import view.Window as w
import time

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 640
MVT = 10
FR = 60

NUMBER_OF_ACTORS = 5
LABORAT_ID = 0


class Game:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print('creating new game instance')
            cls.__instance = super(Game, cls).__new__(cls)
            cls.actor_factory = af.Actor_Factory(NUMBER_OF_ACTORS)
            cls.player = cls.actor_factory.get_actor(0)
            cls.window = w.Window(SCREEN_WIDTH, SCREEN_HEIGHT, cls.actor_factory)
            cls.game_listener = gl.GameListener()
            cls.running = True
            cls.clock = pygame.time.Clock()
        return cls.__instance

    def new_position_validation(self):
        if self.player.position[0] < 0:
            self.player.position[0] = 0
        elif self.player.position[0] > SCREEN_WIDTH - 64:
            self.player.position[0] = SCREEN_WIDTH - 64
        elif self.player.position[1] < 0:
            self.player.position[1] = 0
        elif self.player.position[1] > SCREEN_HEIGHT - 64:
            self.player.position[1] = SCREEN_HEIGHT - 64

    def run(self):
        while self.running and self.window.game_over == 0:
            pressed_up, pressed_down, pressed_left, pressed_right = self.game_listener.get_input()
            if pressed_left:
                self.player.position[0] -= MVT
            if pressed_right:
                self.player.position[0] += MVT
            if pressed_up:
                self.player.position[1] -= MVT
            if pressed_down:
                self.player.position[1] += MVT
            self.window.update_icons()
            self.clock.tick(FR)
            self.new_position_validation()

        self.window.update_icons()
        time.sleep(3)
