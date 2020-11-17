from model.coord import Coord
class Commande:
    def __init__(self, actor, target_location):
        self.actor = actor.__class__
        self.start_coord = actor.get_position()
        self.target_location = target_location