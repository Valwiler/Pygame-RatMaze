import pygame

class GameListener():

    def __init__(self, jeu):
        self.jeu = jeu

    def get_input(self):
        while self.game.en_marche:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.jeu.en_marche = False
                break
            if keys[pygame.K_UP]:
                self.jeu.joueur.posy -= self.game.MVT
            if keys[pygame.K_DOWN]:
                self.jeu.joueur.posy += self.game.MVT
            if keys[pygame.K_LEFT]:
                self.jeu.joueur.posx -= self.game.MVT
            if keys[pygame.K_RIGHT]:
                self.jeu.joueur.posx += self.game.MVT