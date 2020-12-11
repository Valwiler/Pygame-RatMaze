from model.coord import Coord

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# todo refactor command pour qu'elle retourne :
# todo refactor movement pour qu'elle retourne : une direction(int 0/3) et une animation(0/2)
# todo switch case pour determiner direction du mouvement

class Command:
    def __init__(self, actor, start_coord, target_coord):
        self.actor = actor
        self.start_coord = start_coord
        self.target_coord = target_coord

    class Movement:

        def __init__(self):
            pass

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
