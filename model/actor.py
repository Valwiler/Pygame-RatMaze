class Acteur:

    def __init__(self, sprite, coordinate, color):
        self.is_alive = True
        self.sprite = sprite
        self.position = list(coordinate)
        self.color = color

    def set_alive(self, new_state):
        self.is_alive = new_state

    def set_position(self, coordinate):
        self.position = coordinate
