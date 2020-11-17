from model.coord import Coord


class Command:
    def __init__(self, actor ,start_coord, target_coord):
        self.actor = actor
        self.start_coord = start_coord
        self.target_coord = target_coord
