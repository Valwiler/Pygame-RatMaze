import heapq
import math

from model.coord import Coord


class Pathfinder:
    def __init__(self, maze, invalid_positions_dictionary):
        self.maze = maze
        self.invalid_positions_dictionary = invalid_positions_dictionary

    class Tile_Pathfinding:
        def __init__(self, coordinate, parent=None, occupied=False, h=0):
            self.coordinate = coordinate
            self.parent = parent
            self.occupied = occupied
            self.h = h  # distance of tile to end

        def get_h(self):
            return self.h

        def get_coordinate(self):
            return self.coordinate

        def __lt__(self, other):
            return self.h < other.h

    # def __cmp__(self, other):
    #     return self.h < other.h
    @staticmethod
    def same_coordinate(coordinate_a, coordinate_b):
        return (coordinate_a.get_x() == coordinate_b.get_x()) and \
               (coordinate_a.get_y() == coordinate_b.get_y())

    def is_viable_position(self, tile):
        x = tile.coordinate.get_x()
        y = tile.coordinate.get_y()
        key_coordinate = (x, y)
        return key_coordinate not in self.invalid_positions_dictionary.keys() and (
                self.maze[y][x].get_actor(0).get_type() == 0 or self.maze[y][x].get_actor(0).get_type() == 2)

    @staticmethod
    def manhattan_distance(current_tile, goal_tile):
        return abs((goal_tile.coordinate.x - current_tile.coordinate.x) + (
                goal_tile.coordinate.y - current_tile.coordinate.y))

    @staticmethod
    def euclidian_distance(current_tile, goal_tile):
        return math.sqrt((current_tile.coordinate.get_x() - goal_tile.coordinate.get_x()) ** 2 + (
                current_tile.coordinate.get_y() - goal_tile.coordinate.get_y()) ** 2)

    def adjacent_tiles(self, current_tile):
        current_x = current_tile.coordinate.x
        current_y = current_tile.coordinate.y
        possible_positions = set()
        viable_positions = set()
        possible_positions.add(self.Tile_Pathfinding(Coord(current_x - 1, current_y)))
        possible_positions.add(self.Tile_Pathfinding(Coord(current_x + 1, current_y)))
        possible_positions.add(self.Tile_Pathfinding(Coord(current_x, current_y - 1)))
        possible_positions.add(self.Tile_Pathfinding(Coord(current_x, current_y + 1)))
        for position in possible_positions:
            if self.is_viable_position(position):
                viable_positions.add(position)
        return viable_positions

    # # def get_path(tile):
    #     parent_tile = tile.parent
    #     while parent_tile is not None:
    #         parent_tile = parent_tile.parent
    #
    #     return parent_tile.coordinate

    def find_path(self,starting_cohordinate, goal_coordinate):
        current_tile = self.Tile_Pathfinding(starting_cohordinate)
        goal_tile = self.Tile_Pathfinding(goal_coordinate)
        open_ways = set()
        open_heap = []
        closed_ways = set()
        open_ways.add(current_tile.get_coordinate().get_coord_tuple())
        open_heap.append((0, current_tile))
        i = 0
        while open_ways:
            i += 1
            print("iter" + str(i))
            current_tile = heapq.heappop(open_heap)[1]
            print(current_tile.get_coordinate().get_srt_coord())
            if self.same_coordinate(current_tile.get_coordinate(), goal_tile.get_coordinate()):
                parent_tile = current_tile.parent
                while parent_tile.parent is not None:
                    parent_tile = parent_tile.parent
                return parent_tile.coordinate  # return le path trouve
            open_ways.remove(current_tile.get_coordinate().get_coord_tuple())
            closed_ways.add(current_tile.get_coordinate().get_coord_tuple())
            adj_tiles = self.adjacent_tiles(current_tile)
            for tile in adj_tiles:
                if tile.get_coordinate().get_coord_tuple() not in closed_ways:
                    tile.h = self.manhattan_distance(tile, goal_tile)
                    if tile.get_coordinate().get_coord_tuple() not in open_ways:
                        open_ways.add(tile.get_coordinate().get_coord_tuple())
                        heapq.heappush(open_heap, (tile.h, tile))
                tile.parent = current_tile
