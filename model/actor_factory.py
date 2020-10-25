import pygame
from pygame.sprite import Sprite

import model.actor as ac

YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

ACTORS_POSITIONS = [(12, 12), (800, 400), (400, 360), (200, 160), (600, 560)]


class Actor_Factory:

    def __init__(self, number_of_actors):
        self.actor_list = self.create_actors(number_of_actors)
        self.groupPlayer = pygame.sprite.group()
        self.groupGoal = pygame.sprite.group()
        self.groupDefeat = pygame.sprite.group()

    def create_actors(self, number_of_actors):
        actor_list = []
        for i in range(number_of_actors):
            if i == 0:
                player = Sprite([64, 64])
                self.groupPlayer.add(player)
                actor_list.append(ac.Actor(player, ACTORS_POSITIONS[i], BLUE))
            elif i == 1:
                cheese = Sprite([64,64])
                self.groupGoal.add(cheese)
                actor_list.append(ac.Actor(cheese, ACTORS_POSITIONS[i], YELLOW))
            else:
                zombie = Sprite([64,64])
                self.groupDefeat.add(zombie)
                actor_list.append(ac.Actor(zombie, ACTORS_POSITIONS[i], GREEN))
        return actor_list

    def get_actor(self, actor_id):
        return self.actor_list[actor_id]

    def get_actors(self):
        return self.actor_list
