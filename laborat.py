from sys import exit
import pygame

LFEN = 640
HFEN = 480
LRECT = 40
HRECT = 20
POSX = 100
POSY = 50

R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
N = (0,0,0)

MVT = 10
FR = 60

class Jeu():
    def __init__(self, lf, hf, lr, hr, posx, posy, couleur):
        self.lf, self.hf = lf, hf
        self.lr, self.hr = lr, hr
        self.posx, self.posy = posx, posy
        self.couleur = couleur
        
        self.fenetre = pygame.display.set_mode((self.lf, self.hf))
        
        self.en_marche = True
        self.horloge = pygame.time.Clock()
        
    def executer(self):
        while self.en_marche:
            self.traiter_donnees()
            self.actualiser()
            self.rendre()
            self.horloge.tick(FR)
            
    def traiter_donnees(self):
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.en_marche = False
                break
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_r:
                    self.couleur = R
                elif evenement.key == pygame.K_g:
                    self.couleur = G
                elif evenement.key == pygame.K_b:
                    self.couleur = B
                elif evenement.key == pygame.K_RIGHT:
                    self.posx += MVT
                elif evenement.key == pygame.K_LEFT:
                    self.posx -= MVT
                elif evenement.key == pygame.K_DOWN:
                    self.posy += MVT
                elif evenement.key == pygame.K_UP:
                    self.posy -= MVT

    def actualiser(self):
        pass
        
    def rendre(self):
        self.fenetre.fill(N)
        pygame.draw.rect(self.fenetre,
                        self.couleur,
                        (self.posx, self.posy, self.lr, self.hr))
        pygame.display.update()


def main():
    pygame.init()
    jeu = Jeu(LFEN, HFEN, LRECT, HRECT, POSX, POSY, R)
    jeu.executer()
    pygame.quit()
    
if __name__ == '__main__':
    exit(main())