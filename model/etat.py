import model.actor as a
from model.coord import Coord as coord

WIDTH = 16
HEIGHT = 9

class Etat:
    def __init__(self):
        self.grid = [[None] * WIDTH for j in range(HEIGHT)]

    def add_actor(self, actor, coordinate):
        self.grid[coordinate.get_x()][coordinate.get_y()] = actor

    def tile_occupied(self, coordinate):
        return self.grid[coordinate.get_x()][coordinate.get_y()] is None

    def get_tile(self, coordinate):
        return self.grid[coordinate.get_x()][coordinate.get_y()]

    def move_actor(self, coord1, coord2):
        self.grid[coord2.get_x()][coord2.get_y()] = self.grid[coord1.get_x()][coord1.get_y()]
        self.grid[coord1.get_x()][coord1.get_y()] = None


if __name__ == '__main__':
    debug = Etat()
    print(debug.grid)
    print(debug)
