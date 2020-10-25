LFEN = 1024
HFEN = 640
LRECT = 64
HRECT = 64
MVT = 10

class Actor:
    def __init__(self, sprite, coordinate, color):
        self.is_alive = True
        self.sprite = sprite
        self.position = list(coordinate)
        self.color = color

    def set_alive(self, new_state):
        self.is_alive = new_state

    def set_position(self, coordinate):
        if (self.position[0] > MVT and self.position[0] < LFEN - (MVT + LRECT)) and (self.position[1] > MVT and self.position[1] < HFEN - (MVT + HRECT)):
            self.position = coordinate