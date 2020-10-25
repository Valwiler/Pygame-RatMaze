import pygame


class Actor():
    def __init__(self, coordinate):
        self.is_alive = True
        self.position = list(coordinate)
        self.color = None

    def set_alive(self, new_state):
        self.is_alive = new_state

    def set_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position


class Player(Actor):
    def __init__(self, coordinate):
        super(Player,self).__init__(coordinate)
        self.color = (0, 0, 255)


class Fromage(Actor):
    def __init__(self, coordinate):
        super(Fromage,self).__init__(coordinate)
        self.color = (255, 255, 0)


class Zombie(Actor):
    def __init__(self, coordinate):
        super(Zombie,self).__init__(coordinate)
        self.color = (0, 255, 0)
