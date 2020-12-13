from model.coord import Coord

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

DOWN_DIRECTION = {(-1, -1), (0, -1), (1, -1)}
UP_DIRECTION = {(-1, 1), (0, 1), (1, 1)}
LEFT_DIRECTION = (-1, 0)
RIGHT_DIRECTION = (1, 0)


class Command:
    def __init__(self, actor, start_coord, target_coord, tick):
        self.actor = actor
        self.start_coord = start_coord
        self.target_coord = target_coord
        self.direction = self.define_movement_direction(start_coord, target_coord)

    def define_movement_direction(self, old_position, new_position):
        direction_modifier = (old_position.get_x() - new_position.get_x(), old_position.get_y() - new_position.get_y())
        print(direction_modifier)
        if direction_modifier in UP_DIRECTION:
            return UP
        elif direction_modifier in DOWN_DIRECTION:
            return DOWN
        elif direction_modifier is LEFT_DIRECTION:
            return LEFT
        elif direction_modifier is RIGHT:
            return RIGHT
        else:
            return UP

    def define_move2(self, old_pso, new_pos):
        list_position_possible = list()
        list_position_possible.append(DOWN_DIRECTION)
        list_position_possible.append(UP_DIRECTION)
        list_position_possible.append(RIGHT_DIRECTION)
        list_position_possible.append(LEFT_DIRECTION)

        for couple in list_position_possible:
            if old_pso.get_x() + couple[0] == new_pos.get_x() and old_pso.get_y() + couple[1] == new_pos.get_y():
                pass