import random as rand
from model.actor_factory import Actor_Factory as Factory
import model.actor as actor
from model.command import Command
from model.coord import Coord as coord, Coord
from model.tile import Tile_Game as tile_game
from model.pathfinder import Pathfinder as Pathfinder

WIDTH = 16
HEIGHT = 9
NUMBER_OF_ZOMBIES = 3
ZOMBIE_DIFFICULTY = 10

FOCUSED_ACTOR = 0

FLOOR = 0
WALL = 1
CHEESE = 2
ZOMBIE = 3
PLAYER = 4


def is_wall(target_actor):
    return isinstance(target_actor, actor.Wall)


def is_floor(target_actor):
    return isinstance(target_actor, actor.Floor)


def is_zombie(target_actor):
    return isinstance(target_actor, actor.Zombie)


def is_cheese(target_actor):
    return isinstance(target_actor, actor.Cheese)


def is_player(target_actor):
    return isinstance(target_actor, actor.Player)


def get_player_input(coordinate, game_listener):
    pressed_up, pressed_down, pressed_left, pressed_right = game_listener.get_input()
    new_coordinate = Coord(coordinate.get_x(), coordinate.get_y())
    if pressed_left:
        new_coordinate.set_x(coordinate.get_x() - 1)
    if pressed_right:
        new_coordinate.set_x(coordinate.get_x() + 1)
    if pressed_up:
        new_coordinate.set_y(coordinate.get_y() - 1)
    if pressed_down:
        new_coordinate.set_y(coordinate.get_y() + 1)
    return new_coordinate


def is_tile_containing_moving_actor(current_actor):
    return is_player(current_actor) or is_zombie(current_actor)


def can_zombie_move(tick):
    return tick % ZOMBIE_DIFFICULTY is 0


class Etat:
    def __init__(self):
        self.grid = [[tile_game(coord(x, y)) for x in range(WIDTH)] for y in range(HEIGHT)]
        self.player_coordinate = None
        self.player = None
        self.win = False
        self.loose = False
        self.tile_changed = set()
        self.build_maze()
        self.invalid_positions_dictionary = self.invalid_positions()
        self.pathfinder = Pathfinder(self.grid, self.invalid_positions_dictionary)

    def add_actor(self, actor, coordinate):
        self.grid[coordinate.get_y()][coordinate.get_x()].set_actor(actor)

    def get_map_diff(self):
        return self.tile_changed

    def get_tile(self, coordinate):
        return self.grid[coordinate.get_y()][coordinate.get_x()]

    def move_actor(self, old_coordinate, new_coordinate, current_actor):
        self.grid[new_coordinate.get_y()][new_coordinate.get_x()].set_actor(
            self.grid[old_coordinate.get_y()][old_coordinate.get_x()].get_actor())
        self.grid[old_coordinate.get_y()][old_coordinate.get_x()].empty_tile()
        self.tile_changed.add((old_coordinate.get_x(), old_coordinate.get_y()))
        self.tile_changed.add((new_coordinate.get_x(), new_coordinate.get_y()))
        if is_player(current_actor):
            self.player_coordinate = new_coordinate

    def get_grid(self):
        return self.grid

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
                    self.player = self.get_tile(a_pos).get_actor()
                    self.player_coordinate = a_pos

    def update_grid(self, tick, game_listener):
        self.tile_changed.clear()
        for y, row in enumerate(self.grid):
            for x, current_tile in enumerate(row):
                if self.loose or self.win:
                    break
                current_coordinate = current_tile.get_coordinate()
                if (x, y) not in self.tile_changed:
                    current_actor = current_tile.get_actor(FOCUSED_ACTOR)
                    if is_tile_containing_moving_actor(current_actor):
                        new_coordinate = current_coordinate
                        if is_zombie(current_actor):
                            if can_zombie_move(tick):
                                new_coordinate = self.pathfinder.find_path(current_actor, current_coordinate,
                                                                           self.player_coordinate)
                        elif is_player(current_actor):
                            new_coordinate = self.pathfinder.verify_new_position(current_actor,
                                                                                 get_player_input(
                                                                                     current_coordinate,
                                                                                     game_listener),
                                                                                 current_coordinate)
                        self.execute_command(Command(current_actor, current_coordinate, new_coordinate))

    def execute_command(self, command):
        if is_player(command.actor):
            self.win = self.is_player_on_cheese(command.target_coord)
            if not self.win:
                self.loose = self.is_player_on_zombie(command.target_coord)
        elif is_zombie(command.actor):
            self.loose = self.is_zombie_on_player(command.target_coord)
        self.move_actor(command.start_coord, command.target_coord, command.actor)
        command.actor.update_sprite(command.direction)

    def is_player_on_cheese(self, target_coordinate):
        return is_cheese(self.get_tile(target_coordinate).get_actor())

    def is_player_on_zombie(self, target_coordinate):
        return is_zombie(self.get_tile(target_coordinate).get_actor())

    def is_zombie_on_player(self, target_coordinate):
        return is_player(self.get_tile(target_coordinate).get_actor())

    def invalid_positions(self):
        invalid_positions_dictionary = {}
        for y in range(-2, HEIGHT + 1, 1):
            invalid_positions_dictionary[(WIDTH, y)] = False
            invalid_positions_dictionary[(-1, y)] = False
        for x in range(-2, WIDTH + 1, 1):
            invalid_positions_dictionary[(x, -1)] = False
            invalid_positions_dictionary[(x, HEIGHT)] = False

        for y, row in enumerate(self.grid):
            for x, current_tile in enumerate(row):
                if is_wall(self.grid[y][x].get_actor()):
                    invalid_positions_dictionary[(x, y)] = False
        return invalid_positions_dictionary
