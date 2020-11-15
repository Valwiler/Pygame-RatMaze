import model.actor as a


class Etat:
    def __init__(self):
        self.grid = [[None] * 16 for j in range(9)]

    def add_actor(self, actor, x, y):
        self.grid [x][y] = actor

    def tile_occupied(self, x, y):
        return self.grid [x][y] == None

    def get_actor(self, x, y):
        return self.grid[x][y]

    def move_actor(self, x1,y1, x2,y2):
        self.grid[x2][y2] = self.grid[x1][y1]
        self.grid[x1][y1] = None



if __name__ == '__main__':
    debug = Etat()
    print(debug)
