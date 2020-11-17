class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coord(self):
        return self.x, self.y

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

    def modify_coordinate(self, x_modifier, y_modifier):
        self.x = self.x + x_modifier
        self.y = self.y + y_modifier

    def print(self):
        print('x' + str(self.x))
        print('y' + str(self.y))