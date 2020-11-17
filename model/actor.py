from abc import abstractmethod
from model.coord import Coord
from controller.game_listener import Game_Listener as gl
from model.command import Command as command
import math

WALL = 1
PLAYER = 2
ZOMBIE = 3
CHEESE = 4

class Actor:
    def __init__(self):
        self.is_alive = True
        self.type = None

    def set_alive(self, new_state):
        self.is_alive = new_state

    def get_alive(self):
        return self.is_alive

    def get_type(self):
        return self.type

    def update(self, position):
        return command(self, position, position)


class Player(Actor):
    def __init__(self):
        super(Player, self)
        self.type = 2

    def update(self, position):
        pressed_up, pressed_down, pressed_left, pressed_right = gl.get_input()
        temp_position = position
        if pressed_left:
            temp_position.set_x(temp_position.get_x() - 1)
        if pressed_right:
            temp_position.set_x(temp_position.get_x() + 1)
        if pressed_up:
            temp_position.set_y(temp_position.get_y() - 1)
        if pressed_down:
            temp_position.set_y(temp_position.get_y() + 1)
        return command(self, position, [temp_position])


class Zombie(Actor):
    def __init__(self):
        super(Zombie, self)
        self.type = 3

    def update(self, position, player_position):
        possible_positions = []
        current_x, current_y = position.get_coord()
        # left
        possible_positions.append(Coord(current_x - 1, current_y))
        # up-left
        possible_positions.append(Coord(current_x - 1, current_y - 1))
        # up
        possible_positions.append(Coord(current_x, current_y - 1))
        # up-right
        possible_positions.append(Coord(current_x + 1, current_y - 1))
        # right
        possible_positions.append(Coord(current_x + 1, current_y))
        # down-right
        possible_positions.append(Coord(current_x + 1, current_y + 1))
        # down
        possible_positions.append(Coord(current_x, current_y + 1))
        # down-left
        possible_positions.append(Coord(current_x - 1, current_y + 1))

        array_length = len(possible_positions)
        for i in range(array_length - 1):
            for j in range(0, array_length - i - 1):
                if self.is_further_to_player(possible_positions[j], possible_positions[j + 1], player_position):
                    possible_positions[j], possible_positions[j + 1] = possible_positions[j + 1], possible_positions[j]
        return command(self, position,possible_positions)

    def is_further_to_player(self, position_focused, next_position, player_position):
        objectif_x, objectif_y = player_position.get_x(), player_position.get_y()
        focus_x, focus_y = position_focused.get_x(), position_focused.get_y()
        compared_x, compared_y = next_position.get_x(), next_position.get_y()
        focused_distance = math.sqrt((focus_x - objectif_x) ** 2 + (focus_y - objectif_y) ** 2)
        compared_distance = math.sqrt((compared_x - objectif_x) ** 2 + (compared_y - objectif_y) ** 2)
        return focused_distance > compared_distance


class Wall(Actor):
    def __init__(self):
        super(Wall, self)
        self.type = 1


class Fromage(Actor):
    def __init__(self):
        super(Fromage, self)
        self.type = 4
