UP = 2
RIGHT = 1
DOWN = 0
LEFT = 3

DOWN_DIRECTION = {(0, -1)}
UP_DIRECTION = {(0, 1)}
LEFT_DIRECTION = {(-1, 0), (-1, -1), (-1, 1)}
RIGHT_DIRECTION = {(1, 0), (1, 1), (1, -1)}


class Command:
    def __init__(self, actor, start_coord, target_coord):
        self.actor = actor
        self.start_coord = start_coord
        self.target_coord = target_coord
        self.define_movement_direction(start_coord, target_coord)
        self.direction = actor.direction

    def define_movement_direction(self, old_pos, new_pos):
        list_position_possible = list()
        list_position_possible.append(DOWN_DIRECTION)
        list_position_possible.append(UP_DIRECTION)
        list_position_possible.append(RIGHT_DIRECTION)
        list_position_possible.append(LEFT_DIRECTION)

        for direction in list_position_possible:
            for couple in direction:
                x = couple[0]
                y = couple[1]
                if old_pos.get_x() + x == new_pos.get_x() and old_pos.get_y() + y == new_pos.get_y():
                    if couple in UP_DIRECTION:
                        self.actor.direction = UP
                    elif couple in RIGHT_DIRECTION:
                        self.actor.direction = RIGHT
                    elif couple in DOWN_DIRECTION:
                        self.actor.direction = DOWN
                    elif couple in LEFT_DIRECTION:
                        self.actor.direction = LEFT
                    else:
                        self.actor.direction = self.actor.direction
                else:
                    self.actor.direction = self.actor.direction
