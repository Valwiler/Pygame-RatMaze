import pygame


class GameListener():


    def __init__(self, laborat, SCREEN_WIDTH, SCREEN_HEIGHT, MVT):
        self.laborat = laborat
        self.scren_w = SCREEN_WIDTH
        self.screen_h = SCREEN_HEIGHT
        self.mvt = MVT


    def get_input(self):
        for evenement in pygame.event.get():
            temp_laborat_position = self.laborat.get_position()
            if evenement.type == pygame.QUIT:
                self.game.running = False   #TODO: arreter le jeu sans erreur a la fin
                break
            elif evenement.type == pygame.KEYDOWN:  #TODO: deplacer en continu et pas a la pression (voir pygame.KEYUP)
                if evenement.key == pygame.K_RIGHT:
                    self.laborat.position[0] += self.mvt
                elif evenement.key == pygame.K_LEFT:
                    self.laborat.position[0] -= self.mvt
                elif evenement.key == pygame.K_DOWN:
                    self.laborat.position[1] += self.mvt
                elif evenement.key == pygame.K_UP:
                    self.laborat.position[1] -= self.mvt

            print(str(temp_laborat_position[0]) + " " + str(temp_laborat_position[1]))
            self.new_position_validation()


    def new_position_validation(self):
        if self.laborat.position[0] < 0:
            self.laborat.position[0] = 0
        elif self.laborat.position[0] > self.scren_w - 64:
            self.laborat.position[0] = self.scren_w - 64
        elif self.laborat.position[1] < 0:
            self.laborat.position[1]=0
        elif self.laborat.position[1] > self.screen_h - 64:
            self.laborat.position[1]= self.screen_h - 64

