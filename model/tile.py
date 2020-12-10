class Tile:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.actors = list()
        self.used = False

    def is_used(self):
        return self.used

    def get_actor(self, index):
        return self.actors[index]

    def set_used(self):
        self.used = True

    def set_actor(self, actor):
        self.actors.insert(0, actor)

    def empty_tile(self):
        if len(self.actors) > 1:
            self.actors.pop(0)

    def reset(self):
        self.used = False

    def get_coordinate(self):
        return self.coordinate
