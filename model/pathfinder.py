import heapq
from model import etat as etat
from model.tile import Tile_Pathfinding as tile_path_finding
import model.actor as actor

from model.coord import Coord


class Pathfinder:
    def __init__(self, maze, invalid_positions_dictionary):
        self.maze = maze
        self.invalid_positions_dictionary = invalid_positions_dictionary

    def is_viable_position(self, target_actor, coordinate):
        x = coordinate.get_x()
        y = coordinate.get_y()
        key_coordinate = (x, y)
        if key_coordinate not in self.invalid_positions_dictionary.keys():
            target_tile_actor = self.maze[y][x].get_actor()
            if etat.is_zombie(target_actor):
                return not etat.is_zombie(target_tile_actor) and not etat.is_cheese(target_tile_actor)
            else:
                return True

    @staticmethod
    def manhattan_distance(current_tile, goal_tile):
        return abs((goal_tile.coordinate.x - current_tile.coordinate.x) + (
                goal_tile.coordinate.y - current_tile.coordinate.y))

    def adjacent_tiles(self, zombie, current_tile):
        current_x = current_tile.coordinate.x
        current_y = current_tile.coordinate.y
        possible_positions = list()
        viable_positions = list()
        possible_positions.append(tile_path_finding(Coord(current_x, current_y - 1)))
        possible_positions.append(tile_path_finding(Coord(current_x, current_y + 1)))
        possible_positions.append(tile_path_finding(Coord(current_x - 1, current_y)))
        possible_positions.append(tile_path_finding(Coord(current_x - 1, current_y + 1)))
        possible_positions.append(tile_path_finding(Coord(current_x - 1, current_y - 1)))
        possible_positions.append(tile_path_finding(Coord(current_x + 1, current_y)))
        possible_positions.append(tile_path_finding(Coord(current_x + 1, current_y + 1)))
        possible_positions.append(tile_path_finding(Coord(current_x + 1, current_y - 1)))
        for position in possible_positions:
            if self.is_viable_position(zombie, position.get_coordinate()):
                viable_positions.append(position)
        return viable_positions

    def verify_new_position(self, player, new_position, old_position):
        if self.is_viable_position(player, new_position):
            return new_position
        else:
            return old_position

    def get_path(self, tile):
        if tile.parent.parent is not None:
            tile = tile.parent
            while tile.parent.parent is not None:
                tile = tile.parent
        return tile.get_coordinate()

    def find_path(self, zombie, starting_coordinate, goal_coordinate):
        current_tile = tile_path_finding(starting_coordinate)
        goal_tile = tile_path_finding(goal_coordinate)
        open_ways = set()
        open_heap = []
        closed_ways = set()
        open_ways.add((current_tile.get_coordinate().get_x(), current_tile.get_coordinate().get_y()))
        open_heap.append((0, current_tile))
        while open_ways:
            current_tile = heapq.heappop(open_heap)[1]
            tile_coordinate = (current_tile.get_coordinate().get_x(), current_tile.get_coordinate().get_y())
            if current_tile.get_coordinate().is_same_coordinate(goal_tile.get_coordinate()):
                return self.get_path(current_tile)  # return le path trouve
            open_ways.remove(tile_coordinate)
            closed_ways.add(tile_coordinate)
            adj_tiles = self.adjacent_tiles(zombie, current_tile)
            for tile in adj_tiles:
                tile_coordinate = (tile.get_coordinate().get_x(), tile.get_coordinate().get_y())
                if tile_coordinate not in closed_ways:
                    tile.h = self.manhattan_distance(tile, goal_tile)
                    if tile_coordinate not in open_ways:
                        open_ways.add(tile_coordinate)
                        heapq.heappush(open_heap, (tile.h, tile))
                tile.parent = current_tile
