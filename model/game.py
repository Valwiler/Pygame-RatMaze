import pygame
import model.actor_factory as af
import model.player as p
import controller.game_listener as gl
import view.Window as w

MVT = 10
FR = 60

Noir = (0, 0, 0)
Blanc = (255, 255, 255)

NUMBER_OF_ACTORS = 5

class Game:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print('creating new game instace')
            cls.__instance = super(Game, cls).__new__(cls)
            cls.actor_factory = af.Actor_Factory(NUMBER_OF_ACTORS)
            print(cls.actor_factory)
            cls.player = p.Player(cls.actor_factory.get_actor(0))
            print(cls.player.laborat)
            cls.window = w.Window()
            cls.game_listener = gl.GameListener(cls.__instance)
            cls.running = True
            cls.clock = pygame.time.Clock()
        return cls.__instance


    def run(cls):
        while cls.running :
            keys = pygame.key.get_pressed()
