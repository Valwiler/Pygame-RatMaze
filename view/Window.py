import pygame as pg
import view.IconesActeur as i
import model.actor as a

import model.actor_factory as acf


RED = (255,0,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Window:


    def __init__(self, width, height):
        self.ecran = pg.display.set_mode((width, height))

        self.game_over = 0
        self.background_color = (0, 0, 0)
        self.font = pg.font.Font(pg.font.get_default_font(), 32)
        self.text1 = self.font.render('You Win !!!', True, BLACK, WHITE)
        #self.text2 = self.font.render("You Lost :'(", True, BLACK, RED)
        self.text2 = self.font.render("Tickle, Tickle, here come my pickle ;)", True, BLACK, RED)
        self.trect1 = self.text1.get_rect()
        self.trect2 = self.text2.get_rect()
        self.trect1.center = (width // 2, height // 2)
        self.trect2.center = (width // 2, height // 2)
        


    def update_icons(self, act_factory):

        self.ecran.fill(self.background_color)
        for icons in act_factory:
            if  isinstance(icons, a.Player):
                for icone2 in act_factory:
                    if i.IconesActeurs(icons, 64).isinCollision(i.IconesActeurs(icone2, 64)):
                        if isinstance(icone2, a.Zombie):
                            self.background_color = RED
                            icons.set_alive(False)
                            self.game_over = 1
                            self.ecran.blit(self.text2, self.trect2)
                            print('game over')
                            #TODO: arreter deplacement (et afficher YOU LOOSE)
                        elif isinstance(icone2,a.Fromage):
                            self.background_color = WHITE
                            icone2.set_alive(False)
                            self.game_over = 1
                            self.ecran.blit(self.text1, self.trect1)
                            print('Yay, you won !!!')
                            #TODO: arreter deplacement (et afficher YOU WIN)
                        else:
                            pass
            color, rect = i.IconesActeurs(icons, 64).getIcon()
            pg.draw.rect(self.ecran, color, rect)
        pg.display.update()
