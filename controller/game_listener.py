import pygame


class GameListener():

    def __init__(self, game):
        self.game = game

    def get_input(self):
        for evenement in pygame.event.get():
            #INPUT
            if evenement.type == pygame.QUIT:
                self.game.running = False
                break
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_RIGHT:
                    self.game.player.position[0] += self.game.MVT
                elif evenement.key == pygame.K_LEFT:
                    self.game.player.position[0] -= self.game.MVT
                elif evenement.key == pygame.K_DOWN:
                    self.game.player.position[1] += self.game.MVT
                elif evenement.key == pygame.K_UP:
                    self.game.player.position[1] -= self.game.MVT
