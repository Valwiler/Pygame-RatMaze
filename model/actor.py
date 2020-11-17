from abc import abstractmethod
from model.coord import Coord
from controller import game_listener as gl
from model.command import Command as command
import math


class Actor:
    def __init__(self, coordinate):
        self.is_alive = True
        self.position = coordinate
        self.color = None

    def set_alive(self, new_state):
        self.is_alive = new_state

    def set_position(self, new_coordinate):
        self.position = new_coordinate

    def get_position(self):
        return self.position

    def get_alive(self):
        return self.is_alive

    @abstractmethod
    def update(self):
        return command(self, self.position)


class Player(Actor):
    def __init__(self, coordinate):
        super(Player, self).__init__(coordinate)
        self.color = (0, 0, 255)

    def update(self):
        pressed_up, pressed_down, pressed_left, pressed_right = gl.get_input()
        temp_position = self.position.get_coord()
        if pressed_left:
            temp_position.set_x(temp_position.get_x() - 1)
        if pressed_right:
            temp_position.set_x(temp_position.get_x() + 1)
        if pressed_up:
            temp_position.set_y(temp_position.get_y() - 1)
        if pressed_down:
            temp_position.set_y(temp_position.get_y() + 1)
        return command(Player, temp_position)


class Zombie(Actor):
    def __init__(self, coordinate):
        super(Zombie, self).__init__(coordinate)
        self.color = (0, 255, 0)

    def update(self, player_position):
        possible_positions = []
        current_x, current_y = self.position.get_coord()
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
        # dawn-right
        possible_positions.append(Coord(current_x + 1, current_y + 1))
        # dawn
        possible_positions.append(Coord(current_x, current_y + 1))
        # dawn-left
        possible_positions.append(Coord(current_x - 1, current_y + 1))

        array_length = len(possible_positions)
        for i in range(array_length - 1):
            for j in range(0, array_length - i - 1):
                if self.is_further_to_player(possible_positions[j], possible_positions[j + 1], player_position):
                    possible_positions[j], possible_positions[j + 1] = possible_positions[j + 1], possible_positions[j]
        for position in possible_positions:
            print(position.x)
            print(position.y)
            print()
        return possible_positions

    def is_further_to_player(self, position_focused, next_position, player_position):
        objectif_x, objectif_y = player_position.get_x(), player_position.get_y()
        focus_x, focus_y = position_focused.get_x(), position_focused.get_y()
        compared_x, compared_y = next_position.get_x(), next_position.get_y()
        focused_distance = math.sqrt((focus_x - objectif_x) ** 2 + (focus_y - objectif_y) ** 2)
        compared_distance = math.sqrt((compared_x - objectif_x) ** 2 + (compared_y - objectif_y) ** 2)
        return focused_distance > compared_distance


class Wall(Actor):
    def __init__(self, coordinate):
        super(Wall, self).__init__(coordinate)
        self.color = (220, 220, 220)


class Fromage(Actor):
    def __init__(self, coordinate):
        super(Fromage, self).__init__(coordinate)
        self.color = (255, 255, 0)


if __name__ == '__main__':
    zombie = Zombie(Coord(3, 4))
    zombie.update(Coord(10, 2))
