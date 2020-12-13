class Tile:
    def __init__(self, coordinate):
        self.coordinate = coordinate

    def get_coordinate(self):
        return self.coordinate


class Tile_Game(Tile):
    def __init__(self, coordinate):
        super(Tile_Game, self).__init__(coordinate)
        self.actors = list()

    def get_actor(self, index=0):
        return self.actors[index]

    def set_actor(self, actor):
        self.actors.insert(0, actor)

    def empty_tile(self):
        if len(self.actors) > 1:
            self.actors.pop(0)


class Tile_Pathfinding(Tile):
    def __init__(self, coordinate, parent=None, h=0):
        super(Tile_Pathfinding, self).__init__(coordinate)
        self.parent = parent
        self.h = h  # distance of tile to end

    def get_h(self):
        return self.h

    def __lt__(self, other):
        return self.h < other.h
