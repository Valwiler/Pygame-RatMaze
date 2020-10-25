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


    def create_actors(self, number_of_actors):
        actor_list = []
        for i in range(number_of_actors):
            if i == 0:
                actor_list.append(ac.Player( ACTORS_POSITIONS[i]))
            elif i == 1:
                actor_list.append(ac.Fromage( ACTORS_POSITIONS[i]))
            else:
                actor_list.append(ac.Zombie( ACTORS_POSITIONS[i]))
        return actor_list

    def get_actor(self, actor_id):
        return self.actor_list[actor_id]

    def get_actors(self):
        return self.actor_list
