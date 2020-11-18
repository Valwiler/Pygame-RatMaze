import model.actor as ac

YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WALL = 1
PLAYER = 2
ZOMBIE = 3
CHEESE = 4


class Actor_Factory:

    @staticmethod
    def create_actor(type):
        if type is WALL:
            return ac.Wall()
        elif type is PLAYER:
            return ac.Player()
        elif type is ZOMBIE:
            return ac.Zombie()
        elif type is CHEESE:
            return ac.Fromage()