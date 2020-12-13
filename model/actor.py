import pygame
import abc

SPRITE_SIZE = 64
TOP_MARGIN = 5
NUMBER_OF_DIRECTIONS = 4
NUMBER_OF_ANIMATIONS = 3


# TODO bouger les updates de

class Actor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = None

    @abc.abstractmethod
    def get_sprite(self):
        return self.sprite

    def extract_sprites(self, rows_number, columns_number, mutli_sprite_document_path):
        sprite_sheet = pygame.image.load(mutli_sprite_document_path)
        sprites_list = []
        for row in range(rows_number):
            new_sprites_direction = []
            for column in range(columns_number):
                new_sprite_x = row * SPRITE_SIZE + TOP_MARGIN
                new_sprite_y = column * SPRITE_SIZE
                sprite = pygame.Surface([SPRITE_SIZE, SPRITE_SIZE]).convert()
                sprite.set_colorkey((0, 0, 0), 0)
                sprite.blit(sprite_sheet, (0, 0), (new_sprite_x, new_sprite_y, SPRITE_SIZE, SPRITE_SIZE))
                new_sprites_direction.append(sprite)
            sprites_list.append(new_sprites_direction)
        return sprites_list


class Player(Actor):
    def __init__(self):
        super(Player, self).__init__()
        self.sprites = self.extract_sprites(NUMBER_OF_DIRECTIONS, NUMBER_OF_ANIMATIONS, "./sprites/laborat.png")
        self.sprite_counter = 0
        self.sprite = self.sprites[0][self.sprite_counter]

    def update_sprite(self, new_direction):
        self.sprite = self.sprites[new_direction][self.increase_counter()]

    def get_sprite(self):
        return self.sprite


    def increase_counter(self):
        self.sprite_counter += 1
        return self.sprite_counter % 3

class Zombie(Actor):
    def __init__(self):
        super(Zombie, self).__init__()
        self.sprites = self.extract_sprites(NUMBER_OF_DIRECTIONS, NUMBER_OF_ANIMATIONS, "./sprites/zombie.png")
        self.sprite_counter = 0
        self.sprite = self.sprites[0][self.sprite_counter]

    def update_sprite(self, new_direction):
        self.sprite = self.sprites[0][self.increase_counter()]

    def get_sprite(self):
        return self.sprite

    def increase_counter(self):
        self.sprite_counter += 1
        return self.sprite_counter % 3

class Wall(Actor):
    def __init__(self):
        super(Wall, self).__init__()
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/mur_brique.png")),
                                             (SPRITE_SIZE, SPRITE_SIZE))

    def get_sprite(self):
        return self.sprite


class Cheese(Actor):
    def __init__(self):
        super(Cheese, self).__init__()
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/fromage.png")), (SPRITE_SIZE, SPRITE_SIZE))

    def get_sprite(self):
        return self.sprite


class Floor(Actor):
    def __init__(self):
        super(Floor, self)
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/texture_pierre.png")),
                                             (SPRITE_SIZE, SPRITE_SIZE))

    def get_sprite(self):
        return self.sprite
