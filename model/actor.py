from model.coord import Coord
from model.command import Command as command
import math
import pygame

class Actor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.is_alive = True
        self.type = None
        self.sprite = None

    def set_alive(self, new_state):
        self.is_alive = new_state

    def get_alive(self):
        return self.is_alive

    def get_type(self):
        return self.type

    def update(self, position):
        return command(self, position, position)

    def get_sprite(self):
        return self.sprite


class Player(Actor):
    def __init__(self):
        super(Player, self)
        self.type = 2
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/laborat.png")), (64, 64))

    def update(self, position, game_listener):
        pressed_up, pressed_down, pressed_left, pressed_right = game_listener.get_input()
        temp_position = Coord(position.get_x(), position.get_y())
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
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/zombie.png")), (64, 64))

    def update(self, position, player_position):
        possible_positions = []
        current_x, current_y = position.get_coord()
        possible_positions.append(Coord(current_x - 1, current_y))
        possible_positions.append(Coord(current_x - 1, current_y - 1))
        possible_positions.append(Coord(current_x, current_y - 1))
        possible_positions.append(Coord(current_x + 1, current_y - 1))
        possible_positions.append(Coord(current_x + 1, current_y))
        possible_positions.append(Coord(current_x + 1, current_y + 1))
        possible_positions.append(Coord(current_x, current_y + 1))
        possible_positions.append(Coord(current_x - 1, current_y + 1))

        array_length = len(possible_positions)
        for i in range(array_length - 1):
            for j in range(0, array_length - i - 1):
                if self.is_further_to_player(possible_positions[j], possible_positions[j + 1], player_position):
                    possible_positions[j], possible_positions[j + 1] = possible_positions[j + 1], possible_positions[j]
        return command(self, position, possible_positions)

    # calcul de distance entre zombie et joueur
    def is_further_to_player(self, position_focused, next_position, player_position):
        objective_x, objective_y = player_position.get_x(), player_position.get_y()
        focus_x, focus_y = position_focused.get_x(), position_focused.get_y()
        compared_x, compared_y = next_position.get_x(), next_position.get_y()
        focused_distance = math.sqrt((focus_x - objective_x) ** 2 + (focus_y - objective_y) ** 2)
        compared_distance = math.sqrt((compared_x - objective_x) ** 2 + (compared_y - objective_y) ** 2)
        return focused_distance > compared_distance


class Wall(Actor):
    def __init__(self):
        super(Wall, self)
        self.type = 1
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/mur_brique.png")), (64, 64))


class Fromage(Actor):
    def __init__(self):
        super(Fromage, self)
        self.type = 4
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/fromage.png")), (64, 64))

class Tuile_Plancher(Actor):
    def __init__(self):
        super(Tuile_Plancher, self)
        self.type = 0
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/texture_pierre.png")), (64, 64))