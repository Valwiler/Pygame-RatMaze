import heapq
import math

from model.coord import Coord


class Tile:
    def __init__(self, coordinate, parent=None, occupied=False, h=0):
        self.coordinate = coordinate
        self.parent = parent
        self.occupied = occupied
        self.h = h  # distance of tile to end

    def get_h(self):
        return self.h


def same_cohordiante_tile(tile_a, tile_b):
    return (tile_a.coordinate.get_x() == tile_b.coordinate.get_x()) and \
           (tile_a.coordinate.get_y() == tile_b.coordinate.get_y())


def is_viable_position(tile, maze, invalid_positions_dictionary):
    x = tile.coordinate.get_x()
    y = tile.coordinate.get_y()
    key_coordinate = (x, y)
    return key_coordinate not in invalid_positions_dictionary.keys() and maze[y][x].get_actor(0).get_type() == 0


def manhattan_distance(current_tile, goal_tile):
    return (goal_tile.coordinate.x - current_tile.coordinate.x) + (
            goal_tile.coordinate.y - current_tile.coordinate.y)


def euclidian_distance(self, current_tile, goal_tile):
    return math.sqrt((current_tile.coordinate.get_x() - goal_tile.coordinate.get_x()) ** 2 + (
                current_tile.coordinate.get_y() - goal_tile.coordinate.get_y()) ** 2)


def adjacent_tiles(current_tile, maze, invalid_positions_dictionary):
    current_x = current_tile.coordinate.x
    current_y = current_tile.coordinate.y
    possible_positions = set()
    viable_positions = set()
    possible_positions.add(Tile(Coord(current_x - 1, current_y)))
    possible_positions.add(Tile(Coord(current_x + 1, current_y)))
    possible_positions.add(Tile(Coord(current_x, current_y - 1)))
    possible_positions.add(Tile(Coord(current_x, current_y + 1)))
    for position in possible_positions:
        if is_viable_position(position, maze, invalid_positions_dictionary):
            viable_positions.add(position)
    return viable_positions


def find_path(starting_cohordinate, goal_coordinate, maze, invalid_positions_dictionary):
    current_tile = Tile(starting_cohordinate)
    goal_tile = Tile(goal_coordinate)
    invalid_positions_dictionary = invalid_positions_dictionary
    open_ways = set()
    open_heap = []
    closed_ways = set()

    open_ways.add(current_tile)
    open_heap.append((0, current_tile))
    while open_ways:
        current_tile = heapq.heappop(open_heap)[1]
        if same_cohordiante_tile(current_tile, goal_tile):
            pass  # return le path trouve
        open_ways.remove(current_tile)
        closed_ways.add(current_tile)
        adj_tiles = adjacent_tiles(current_tile, maze, invalid_positions_dictionary)
        for tile in adj_tiles:
            if tile not in closed_ways:
                tile.h = euclidian_distance(tile, goal_tile)
                if tile not in open_ways:
                    open_ways.add(tile)
                    heapq.heappush(open_heap, (tile.get_h(), tile))
            tile.parent = current_tile


# def further_to_player(self, position_focused, next_position, player_position):
#     objective_x, objective_y = player_position.get_x(), player_position.get_y()
#     focus_x, focus_y = position_focused.get_x(), position_focused.get_y()
#     compared_x, compared_y = next_position.get_x(), next_position.get_y()
#     focused_distance = math.sqrt((focus_x - objective_x) ** 2 + (focus_y - objective_y) ** 2)
#     compared_distance = math.sqrt((compared_x - objective_x) ** 2 + (compared_y - objective_y) ** 2)
#     return focused_distance > compared_distance

