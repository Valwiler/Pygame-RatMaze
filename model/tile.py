class Tile:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.actors = list()
        self.used = False

    def is_used(self):
        return self.used

    def get_actor(self):
        return self.actors[0]

    def set_used(self):
        self.used = True

    def set_actor(self, actor):
        self.actors.insert(0, actor)

    def empty_tile(self):
        if len(self.actors) > 1:
            self.actors.pop(0)

    def reset(self):
        self.used = False
