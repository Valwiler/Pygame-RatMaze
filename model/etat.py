import model.actor as a
from model.coord import Coord as coord


class Etat:
    def __init__(self):
        self.grid = [[None] * 16 for j in range(9)]

    def add_actor(self, actor, coord):
        self.grid[coord.get_x()][coord.get_y()] = actor

    def tile_occupied(self, coord):
        return self.grid[coord.get_x()][coord.get_y()] is None

    def get_tile(self, coord):
        return self.grid[coord.get_x()][coord.get_y()]

    def move_actor(self, coord1, coord2):
        self.grid[coord2.get_x()][coord2.get_y()] = self.grid[coord1.get_x()][coord1.get_y()]
        self.grid[coord1.get_x()][coord1.get_y()] = None


if __name__ == '__main__':
    debug = Etat()
    print(debug)
