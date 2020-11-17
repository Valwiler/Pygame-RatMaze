import model.actor as a
from model.coord import Coord as coord
import random as rand

WIDTH = 16
HEIGHT = 9

class Etat:
    def __init__(self):
        self.grid = [[0] * WIDTH for j in range(HEIGHT)]
        self.map_config = list()

    def add_actor(self, actor, coordinate):
        self.grid[coordinate.get_x()][coordinate.get_y()] = actor

    def tile_occupied(self, coordinate):
        return self.grid[coordinate.get_x()][coordinate.get_y()] is None

    def get_tile(self, coordinate):
        return self.grid[coordinate.get_x()][coordinate.get_y()]

    def move_actor(self, coord1, coord2):
        self.grid[coord2.get_x()][coord2.get_y()] = self.grid[coord1.get_x()][coord1.get_y()]
        self.grid[coord1.get_x()][coord1.get_y()] = None

    def populate_matrix(self):
        with open('../maps.txt') as r:
            map_matrix = r.readlines()

        new_map = list()
        for lines in map_matrix:
            new_map.append(lines.split())
            if lines == '\n':
                self.map_config.append(new_map)
                new_map.clear()
        selection = rand.randint(0, len(self.map_config) - 1)
        print(selection)



if __name__ == '__main__':
    debug = Etat()
    print(debug.grid)
    debug.populate_matrix()
    print(debug)
