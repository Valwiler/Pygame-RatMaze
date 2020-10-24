from sys import exit
import pygame
from model import jeu as j

LFEN = 1024
HFEN = 640
LRECT = 64
HRECT = 64
POS_PLAYER = [12, 12]
POS_CHEESE = [800, 400]
POS_ZOMBIES = [[200, 160], [400, 360], [600, 560]]

MVT = 10
FR = 60

class Acteur(): #TODO extends sprite, create zombie/fromage/player child, implement ActeursFactory, Move models to seperate script
    def __init__(self, posx, posy, couleur):
        self.posx, self.posy = posx, posy
        self.couleur = couleur
        self.alive = True

        
    def executer(self):
        while self.en_marche:
            self.traiter_donnees()
            self.actualiser()
            self.rendre()
            self.horloge.tick(FR)
            
    def traiter_donnees(self): #Move to controler script
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                self.en_marche = False
                break
            elif evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_ESCAPE:
                    self.en_marche = False
                    break
                elif evenement.key == pygame.K_RIGHT:
                    self.joueur.posx += MVT
                elif evenement.key == pygame.K_LEFT:
                    self.joueur.posx -= MVT
                elif evenement.key == pygame.K_DOWN:
                    self.joueur.posy += MVT
                elif evenement.key == pygame.K_UP:
                    self.joueur.posy -= MVT

    def actualiser(self):
        pass
        
    def rendre(self): #move to view script
        self.fenetre.fill(self.couleur)

        #JOUEUR
        pygame.draw.rect(self.fenetre, self.joueur.couleur, (self.joueur.posx, self.joueur.posy, self.lr, self.hr))
        #FROMAGE
        pygame.draw.rect(self.fenetre,self.fromage.couleur,(self.fromage.posx, self.fromage.posy, self.lr, self.hr))
        #ZOMBIES
        pygame.draw.rect(self.fenetre,self.zombie1.couleur,(self.zombie1.posx, self.zombie1.posy, self.lr, self.hr))
        pygame.draw.rect(self.fenetre,self.zombie2.couleur,(self.zombie2.posx, self.zombie2.posy, self.lr, self.hr))
        pygame.draw.rect(self.fenetre,self.zombie3.couleur,(self.zombie3.posx, self.zombie3.posy, self.lr, self.hr))

        pygame.display.update()


def main():
    pygame.init()
    pygame.display.set_caption('Laborat')
    jeu = j.Jeu(LFEN, HFEN, LRECT, HRECT)
    jeu.executer()
    pygame.quit()
    
if __name__ == '__main__':
    exit(main())