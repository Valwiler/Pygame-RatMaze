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
            print(cls.actor_factory)
            cls.window = w.Window(SCREEN_WIDTH, SCREEN_HEIGHT)
            cls.game_listener = gl.GameListener(cls.actor_factory.get_actor(0), SCREEN_WIDTH, SCREEN_HEIGHT, MVT)
            cls.running = True
            cls.clock = pygame.time.Clock()
        return cls.__instance

    def run(self):
        while self.running and self.window.game_over == 0:
            self.window.update_icons(self.actor_factory.get_actors())
            self.game_listener.get_input()
            self.clock.tick(FR)


        self.window.update_icons(self.actor_factory.get_actors())
        time.sleep(10)
        pygame.quit()