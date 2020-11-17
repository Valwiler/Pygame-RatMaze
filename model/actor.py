from abc import abstractmethod
from model.coord import Coord
from controller import game_listener as gl

class Actor:
    def __init__(self, coordinate):
        self.is_alive = True
        self.position = Coord(coordinate[0], [1])
        self.color = None

    def set_alive(self, new_state):
        self.is_alive = new_state

    def set_position(self, new_position):
        self.position = new_position

    def get_position(self):
        return self.position

    def get_alive(self):
        return self.is_alive

    @abstractmethod
    def update(self):
        return None


class Player(Actor):
    def __init__(self, coordinate):
        super(Player, self).__init__(coordinate)
        self.color = (0, 0, 255)

    def update(self):
        pressed_up, pressed_down, pressed_left, pressed_right = gl.get_input()
        if pressed_left:
            return Coord()
        if pressed_right:
        if pressed_up:
        if pressed_down:


class Wall(Actor):
    def __init__(self, coordinate):
        super(Wall, self).__init__(coordinate)
        self.color = (220, 220, 220)

class Fromage(Actor):
    def __init__(self, coordinate):
        super(Fromage, self).__init__(coordinate)
        self.color = (255, 255, 0)


class Zombie(Actor):
    def __init__(self, coordinate):
        super(Zombie, self).__init__(coordinate)
        self.color = (0, 255, 0)
