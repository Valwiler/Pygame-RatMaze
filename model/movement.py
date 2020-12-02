UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Movement:

    def __init__(self, id, position_modifier, current_position):
        self.id = id
        self.position_modifier = position_modifier
        self.current_position = current_position
        self.new_position = self.current_position + position_modifier

    def get_movement_id(self):
        return self.id

    def get_position_modifier(self):
        return self.position_modifier

    def get_new_position(self):
        return self.current_position

class left_movement(Movement):
    def __init__(self, current_position):
        super(LEFT, (0, -1), current_position)


class up_movement(Movement):
    def __init__(self, current_position):
        super(UP, (-1, 0), current_position)


class right_movement(Movement):
    def __init__(self, current_position):
        super(RIGHT, (0, 1), current_position)


class down_movement(Movement):
    def __init__(self, current_position):
        super(DOWN, (1, 0), current_position)
