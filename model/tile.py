class Tile:
    def __init__(self, coordinate):
        self.coordinate = coordinate
        self.actor = None
        self.used = False

    def is_used(self):
        return self.used

    def get_actor(self):
        return self.actor

    def set_used(self):
        self.used = True

    def set_actor(self, actor):
        self.actor = actor

    def reset(self):
        self.used = False
