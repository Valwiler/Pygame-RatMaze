class Tile:
    def __init__(self, coordinate):
        self.coordinate = coordinate

    def get_coordinate(self):
        return self.coordinate


class Tile_Game(Tile):
    def __init__(self, coordinate):
        super(coordinate, self).__init__()
        self.actors = list()

    def get_actor(self, index):
        return self.actors[index]

    def set_actor(self, actor):
        self.actors.insert(0, actor)

    def empty_tile(self):
        if len(self.actors) > 1:
            self.actors.pop(0)


class Tile_Pathfinding(Tile):
    def __init__(self, coordinate, parent=None, h=0):
        super(coordinate, self).__init__()
        self.parent = parent
        self.h = h  # distance of tile to end

    def get_h(self):
        return self.h

    def __lt__(self, other):
        return self.h < other.h
