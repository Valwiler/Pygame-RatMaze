import pygame
import model.etat as etat

SPRITE_SIZE = 64
TOP_MARGIN = 5
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# TODO bouger les updates de

class Actor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.type = None
        self.sprite = None
        # self.direction = 0

    def get_type(self):
        return self.type

    # def update(self, position):
    #     return command(self, position, position)

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
        self.type = etat.PLAYER
        self.sprites = self.extract_sprites(4, 3, "./sprites/laborat.png")
        self.sprite = self.sprites[0][0]

    def update_sprite(self, new_direction, animation):
        self.sprite = self.sprites[new_direction][animation]


class Zombie(Actor):
    def __init__(self):
        super(Zombie, self).__init__()
        self.type = etat.ZOMBIE
        self.sprites = self.extract_sprites(4, 3, "./sprites/zombie.png")
        self.sprite = self.sprites[0][0]

    # TODO prend la direction de la commnande et le nombre de tick pour set la sprite
    #
    # def set_direction(self, new_direction, animation):
    #     self.sprite = self.sprites[new_direction][animation]

    # def update(self, position, new_position):
    #     self.update_sprite()
    #     return command(self, position, [new_position])
    def update_sprite(self, new_direction, animation):
        self.sprite = self.sprites[new_direction][animation]


class Wall(Actor):
    def __init__(self):
        super(Wall, self)
        self.type = etat.WALL
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/mur_brique.png")),
                                             (SPRITE_SIZE, SPRITE_SIZE))


class Fromage(Actor):
    def __init__(self):
        super(Fromage, self)
        self.type = etat.CHEESE
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/fromage.png")), (SPRITE_SIZE, SPRITE_SIZE))


class Tuile_Plancher(Actor):
    def __init__(self):
        super(Tuile_Plancher, self)
        self.type = etat.FLOOR
        self.sprite = pygame.transform.scale((pygame.image.load("./sprites/texture_pierre.png")),
                                             (SPRITE_SIZE, SPRITE_SIZE))
