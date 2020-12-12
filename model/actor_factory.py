import model.actor as ac
import model.etat as etat

class Actor_Factory:

    @staticmethod
    def create_actor(actor_type):
        if actor_type is etat.FLOOR:
            return ac.Tuile_Plancher()
        elif actor_type is etat.WALL:
            return ac.Wall()
        elif actor_type is etat.PLAYER:
            return ac.Player()
        elif actor_type is etat.ZOMBIE:
            return ac.Zombie()
        elif actor_type is etat.CHEESE:
            return ac.Fromage()
