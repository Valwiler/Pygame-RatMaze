import pygame

MVT = 10
FR = 60

Jaune = (255,255,0)
Rouge = (255,0,0)
Vert = (0,255,0)
Bleu = (0,0,255)
Noir = (0,0,0)
Blanc = (255,255,255)


class Jeu:

    __instance = None

    def __init__(self, lf, hf, lr, hr):
        raise RuntimeError('Call instance() instead')

    def instance(self, cls):
        if cls.__instance is not None:
            return cls.__instance
        else:
            self.player
            self.actor_factory
            self.player
            self.window


            self.lf, self.hf = lf, hf
            self.lr, self.hr = lr, hr
            self.couleur = Noir

            self.joueur = Acteur(POS_PLAYER[0], POS_PLAYER[1], Bleu)
            self.fromage = Acteur(POS_CHEESE[0], POS_CHEESE[1], Jaune)
            self.zombie1 = Acteur(POS_ZOMBIES[0][0], POS_ZOMBIES[0][1], Vert)
            self.zombie2 = Acteur(POS_ZOMBIES[1][0], POS_ZOMBIES[1][1], Vert)
            self.zombie3 = Acteur(POS_ZOMBIES[2][0], POS_ZOMBIES[2][1], Vert)

            self.fenetre = pygame.display.set_mode((self.lf, self.hf))

            self.en_marche = True
            self.horloge = pygame.time.Clock()