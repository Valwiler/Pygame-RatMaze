from sys import exit
import pygame

LFEN = 1024
HFEN = 640
LRECT = 64
HRECT = 64
POSX_PLAYER = 12
POSY_PLAYER = 12
POSX_CHEESE = 800
POSY_CHEESE = 400
POS_ZOMBIES = [[200,160],[400,360],[600,560]]

Jaune = (255,255,0)
Rouge = (255,0,0)
Vert = (0,255,0)
Bleu = (0,0,255)
Noir = (0,0,0)
Blanc = (255,255,255)

MVT = 10
FR = 60

class Acteur():
    def __init__(self, posx, posy, couleur):
        self.posx, self.posy = posx, posy
        self.couleur = couleur
        self.alive = True

class Jeu():
    def __init__(self, lf, hf, lr, hr):
        self.lf, self.hf = lf, hf
        self.lr, self.hr = lr, hr
        self.couleur = Noir

        self.joueur = Acteur(POSX_PLAYER, POSY_PLAYER, Bleu)
        self.fromage = Acteur(POSX_CHEESE, POSY_CHEESE, Jaune)
        self.zombie1 = Acteur(POS_ZOMBIES[0][0],POS_ZOMBIES[0][1], Vert)
        self.zombie2 = Acteur(POS_ZOMBIES[1][0],POS_ZOMBIES[1][1], Vert)
        self.zombie3 = Acteur(POS_ZOMBIES[2][0],POS_ZOMBIES[2][1], Vert)
        
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
        
    def rendre(self):
        self.fenetre.fill(self.couleur)

        #JOUEUR
        pygame.draw.rect(self.fenetre,self.joueur.couleur,(self.joueur.posx, self.joueur.posy, self.lr, self.hr))
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
    jeu = Jeu(LFEN, HFEN, LRECT, HRECT)
    jeu.executer()
    pygame.quit()
    
if __name__ == '__main__':
    exit(main())