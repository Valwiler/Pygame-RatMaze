class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # def get_srt_coord(self):
    #     return "X: " + str(self.x) + " Y: " + str(self.y)