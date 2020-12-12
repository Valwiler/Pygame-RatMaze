import random as rand
from model.actor_factory import Actor_Factory as Factory
import model.actor as Actor
from model.command import Command
from model.coord import Coord as coord, Coord
from model.tile import Tile as tile
from model.pathfinder import Pathfinder as Pathfinder

WIDTH = 16
HEIGHT = 9
NUMBER_OF_ZOMBIES = 3
ZOMBIE_DIFFICULTY = 10

FLOOR = 0
WALL = 1
CHEESE = 2
ZOMBIE = 3
PLAYER = 4


class Etat:
    def __init__(self):
        self.grid = [[tile(coord(x, y)) for x in range(WIDTH)] for y in range(HEIGHT)]
        # todo remplacer par un pointeur vers playeur deirectement
        self.player_coordinate = None
        self.win = False
        self.loose = False
        self.tile_changed = set()
        self.build_maze()
        self.invalid_positions_dictionary = self.invalid_positions()
        self.pathfinder = Pathfinder(self.grid, self.invalid_positions_dictionary)

    def add_actor(self, actor, coordinate):
        self.grid[coordinate.get_y()][coordinate.get_x()].set_actor(actor)

    def tile_occupied(self, coordinate):
        occupied = False
        if not isinstance(self.grid[coordinate.get_y()][coordinate.get_x()].get_actor(0), Actor.Tuile_Plancher):
            occupied = True
        return occupied

    def get_map_diff(self):
        return self.tile_changed

    def clear_map_diff(self):
        self.tile_changed.clear()

    def get_tile(self, coordinate):
        return self.grid[coordinate.get_y()][coordinate.get_x()]

    def get_tile_type(self, coordinate):
        return self.grid[coordinate.get_y()][coordinate.get_x()].get_type()

    def move_actor(self, coord1, coord2, actor_type):
        self.grid[coord2.get_y()][coord2.get_x()].set_actor(self.grid[coord1.get_y()][coord1.get_x()].get_actor(0))
        self.grid[coord1.get_y()][coord1.get_x()].empty_tile()
        # self.grid[coord2.get_y()][coord2.get_x()].set_used()
        self.tile_changed.append(coord1)
        self.tile_changed.append(coord2)
        if actor_type == PLAYER:
            self.player_coordinate = coord2

    def get_grid(self):
        return self.grid

    def update_grid(self, tick, game_listener):
        # TODO un set pour concerver les tiles qui on etes utilisees et plus dans la tile en elle meme
        for y, row in enumerate(self.grid):
            for x, current_tile in enumerate(row):
                # if not current_tile.is_used():
                if self.tile_occupied(coord(x, y)):
                    if current_tile.get_actor(0).get_type() == ZOMBIE:
                        if tick % ZOMBIE_DIFFICULTY == 0:
                            new_coord = self.pathfinder.find_path(coord(x, y), self.player_coordinate)
                            self.execute_command(Command(current_tile.get_actor(0), coord(x, y), [new_coord]))
                        else:
                            pass
                    elif current_tile.get_actor(0).get_type() == PLAYER:
                        self.execute_command(current_tile.get_actor(0).update(coord(x, y), game_listener))
        #         executer la commande avec la nouvelle position et l'acteur
        self.reset_tiles()

    #
    # def reset_tiles(self):
    #     for row in self.grid:
    #         for tile in row:
    #             tile.reset()

    def build_maze(self):
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

        game_map = map_config[rand.randint(0, len(map_config) - 1)]
        for y, row in enumerate(game_map):
            for x, actor_type in enumerate(row):
                a_pos = coord(x, y)
                if actor_type is not FLOOR:
                    self.add_actor(Factory.create_actor(FLOOR), a_pos)
                self.add_actor(Factory.create_actor(actor_type), a_pos)
                if actor_type == PLAYER:
                    self.player_coordinate = a_pos

    # vicoty_loose check une fois que le path finder a verifier la case, l'etat regarde les conditions de victoires
    def execute_command(self, command):
        key_coordinate = (command.target_coord.get_x(), command.target_coord.get_y())
        if key_coordinate in self.invalid_positions_dictionary.keys():
            pass
        elif not self.tile_occupied(command.target_coord):
            self.move_actor(command.start_coord, command.target_coord, command.actor.type)
            return
        elif command.actor.type == PLAYER:
            if self.get_tile(command.target_coord).get_actor(0).get_type() is CHEESE:
                self.win = True
            elif self.get_tile(command.target_coord).get_actor(0).get_type() is ZOMBIE:
                self.loose = True
        elif command.actor.type == ZOMBIE:
            if self.get_tile(command.target_coord).get_actor(0).get_type() is PLAYER:
                self.loose = True

    # TODO va dans etat pour verification gestion et verification du deplacement
    def update(position, game_listener):
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
        return temp_position

  # créer un dictionaire de position invalides
    def invalid_positions(self):
        invalid_positions_dictionary = {}
        for y in range(-1, HEIGHT, 1):
            invalid_positions_dictionary[(WIDTH, y)] = False
            invalid_positions_dictionary[(-1, y)] = False
        for x in range(-1, WIDTH, 1):
            invalid_positions_dictionary[(x, -1)] = False
            invalid_positions_dictionary[(x, HEIGHT)] = False

        for y, row in enumerate(self.grid):
            for x, current_tile in enumerate(row):
                if self.tile_occupied(coord(x, y)):
                    if current_tile.get_actor(0).get_type() == WALL:
                        invalid_positions_dictionary[(x, y)] = False
        return invalid_positions_dictionary
