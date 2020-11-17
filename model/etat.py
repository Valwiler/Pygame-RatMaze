import model.actor as a
from model.coord import Coord as coord
import random as rand
from model.actor_factory import Actor_Factory as Factory

WIDTH = 16
HEIGHT = 9
NUMBER_OF_ZOMBIES = 3

NULL = 0
WALL = 1
PLAYER = 2
ZOMBIE = 3
CHEESE = 4


class Etat:
    def __init__(self):
        self.grid = [[None] * WIDTH for j in range(HEIGHT)]
        self.player_coordinate = None
        self.win = False
        self.loose = False
        self.build_walls()

    def add_actor(self, actor, coordinate):
        self.grid[coordinate.get_y()][coordinate.get_x()] = actor

    def tile_occupied(self, coordinate):
        return self.grid[coordinate.get_y()][coordinate.get_x()] is not None

    def get_tile(self, coordinate):
        return self.grid[coordinate.get_y()][coordinate.get_x()]

    def get_tile_type(self, coordinate):
        return self.grid[coordinate.get_y()][coordinate.get_x()].get_type()

    def move_actor(self, coord1, coord2):
        self.grid[coord2.get_y()][coord2.get_x()] = self.grid[coord1.get_y()][coord1.get_x()]
        self.grid[coord1.get_y()][coord1.get_x()] = None


    def get_grid(self):
        return self.grid

    def update_grid(self):
        for y, row in enumerate(self.grid):
            for x, tile in enumerate(row):
                if self.tile_occupied(coord(x, y)):
                    if tile.get_type() == ZOMBIE:
                        self.execute_command(tile.update(coord(x,y),self.player_coordinate))
                    else:
                        self.execute_command(tile.update(coord(x,y)))

    def build_walls(self):
        map_config = list()
        with open('./maps.txt') as r:
            map_matrix = r.readlines()
        new_map = list()
        for lines in map_matrix:
            line = [x.strip() for x in lines.split(',')]
            if not line[0]:
                map_config.append(new_map)
                new_map = list()
            else:
                new_map.append(list(map(int, line)))

        # game_map = map_config[rand.randint(0, len(map_config) - 1)]
        game_map = map_config[0]
        for y, row in enumerate(game_map):
            for x, actor_type in enumerate(row):
                if game_map[y][x] is not NULL:
                    a_pos = coord(x, y)
                    self.add_actor(Factory.create_actor(actor_type), a_pos)
                    if actor_type == PLAYER:
                        self.player_coordinate = a_pos

    def execute_command(self, command):
        if command.actor.type is WALL or command.actor.type is CHEESE:
            return
        for coordinate in command.target_coord:
            if not self.tile_occupied(coordinate):
                self.move_actor(command.start_coord, coordinate)
                return
            elif self.get_tile(coordinate).get_type() is WALL:
                pass
            elif command.actor.type == PLAYER:
                if self.get_tile(coordinate).get_type() is CHEESE:
                    self.win = True
                elif self.get_tile(coordinate).get_type() is ZOMBIE:
                    self.loose = True
            elif command.actor.type == ZOMBIE:
                if self.get_tile(coordinate).get_type() is CHEESE:
                    pass
                elif self.get_tile(coordinate).get_type() is PLAYER:
                    self.loose = True

    def validate_move(self, coord):
        return coord.get_x() < WIDTH and coord.get_y() < HEIGHT
