class Coord:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_coord(self):
        return (self.x, self.y)

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y