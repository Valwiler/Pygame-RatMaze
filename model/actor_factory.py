actors_position = [ (12,12), (800,400), (400,360), (200,160), (600,560)]

class Actor_Factory:

    def __init__(self, number_of_actors):
        self.actor_list = self.create_actors(number_of_actors)


    def create_actors(self, number_of_actors):
        actor_list = []
        for i in range(number_of_actors):
            if i == 0 :
                actor_list [i]

