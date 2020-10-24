import pygame

class GameListener():
    
    def __init__(self, jeu):
        self.game = game

    def get_input(self):
        while self.game.en_marche:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.game.en_marche = False
                break
            if keys[pygame.K_UP]:
                self.game.player.posy -= self.game.MVT
            if keys[pygame.K_DOWN]:
                self.game.player.posy += self.game.MVT
            if keys[pygame.K_LEFT]:
                self.game.player.posx -= self.game.MVT
            if keys[pygame.K_RIGHT]:
                self.game.player.posx += self.game.MVT