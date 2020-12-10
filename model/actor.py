from model.coord import Coord
from model.command import Command as command
import math
import model.pathfinder as pf
import pygame

SPRITE_SIZE = 64
TOP_MARGIN = 5


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

    def define_sprites(self, rows_number, columns_number, mutli_sprite_document_path):
        sprite_sheet = pygame.image.load(mutli_sprite_document_path)
        sprites_list = []
        for row in range(rows_number):
            for column in range(columns_number):
                new_sprite_x = row * SPRITE_SIZE + TOP_MARGIN
                new_sprite_y = column * SPRITE_SIZE
                sprite = pygame.Surface([SPRITE_SIZE, SPRITE_SIZE]).convert()
                sprite.set_colorkey((0, 0, 0), 0)
                sprite.blit(sprite_sheet, (0, 0), (new_sprite_x, new_sprite_y, SPRITE_SIZE, SPRITE_SIZE))
                sprites_list.append(sprite)
        return sprites_list


class Player(Actor):
    def __init__(self):
        super(Player, self)
        self.type = 2
        # self.up_sprites = []
        # self.dawn_sprites = []
        # self.left_sprites = []
        # self.right_sprites = []
        self.sprites = self.define_sprites(4, 3, "./sprites/laborat.png")
        self.sprite = self.sprites[0]
        # self.sprite = pygame.transform.scale((pygame.image.load("./sprites/laborat.png")), (SPRITE_SIZE, SPRITE_SIZE))

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
        self.up_sprites = []
        self.dawn_sprites = []
        self.left_sprites = []
        self.right_sprites = []
        self.sprites = self.define_sprites(4, 3, "./sprites/zombie.png")
        self.sprite = self.sprites[0]
        # self.sprite = pygame.transform.scale((pygame.image.load("./sprites/zombie.png")), (SPRITE_SIZE, SPRITE_SIZE))

    def update(self, position, new_position):
        return command(self, position, [new_position])



    #     possible_positions = []
    #     current_x, current_y = position.get_coord()
    #     possible_positions.append(Coord(current_x - 1, current_y))
    #     possible_positions.append(Coord(current_x - 1, current_y - 1))
    #     possible_positions.append(Coord(current_x, current_y - 1))
    #     possible_positions.append(Coord(current_x + 1, current_y - 1))
    #     possible_positions.append(Coord(current_x + 1, current_y))
    #     possible_positions.append(Coord(current_x + 1, current_y + 1))
    #     possible_positions.append(Coord(current_x, current_y + 1))
    #     possible_positions.append(Coord(current_x - 1, current_y + 1))
    #
    #     array_length = len(possible_positions)
    #     for i in range(array_length - 1):
    #         for j in range(0, array_length - i - 1):
    #             if self.is_further_to_player(possible_positions[j], possible_positions[j + 1], player_position):
    #                 possible_positions[j], possible_positions[j + 1] = possible_positions[j + 1], possible_positions[j]
    #     return command(self, position, possible_positions)
    #
    # # calcul de distance entre zombie et joueur
    #


class Wall(Actor):
    def __init__(self):
        super(Wall, self)
        self.type = 1
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/mur_brique.png")),
                                             (SPRITE_SIZE, SPRITE_SIZE))


class Fromage(Actor):
    def __init__(self):
        super(Fromage, self)
        self.type = 4
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/fromage.png")), (SPRITE_SIZE, SPRITE_SIZE))


class Tuile_Plancher(Actor):
    def __init__(self):
        super(Tuile_Plancher, self)
        self.type = 0
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/texture_pierre.png")),
                                             (SPRITE_SIZE, SPRITE_SIZE))
