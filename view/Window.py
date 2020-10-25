import pygame as pg
import view.IconesActeur as i
import model.actor as a

import model.actor_factory as acf

class Window:


    def __init__(self, width, height):
        self.ecran = pg.display.set_mode((width, height))
        self.background_color = (0, 0, 0)


    def update_icons(self, act_factory):
        self.ecran.fill(self.background_color)
        for icons in act_factory:
            if  isinstance(icons, a.Player):
                for icone2 in act_factory:
                    if i.IconesActeurs(icons, 64).isinCollision(i.IconesActeurs(icone2, 64)):
                        if isinstance(icone2, a.Zombie):
                            self.background_color = (255,0,0)
                            icons.set_alive(False)
                            print('game over')
                            #TODO: arreter deplacement (et afficher YOU LOOSE)
                        elif isinstance(icone2,a.Fromage):
                            self.background_color = (255,255,255)
                            print('Yay, you won !!!')
                            #TODO: arreter deplacement (et afficher YOU WIN)
                        else:
                            pass
            color, rect = i.IconesActeurs(icons, 64).getIcon()
            pg.draw.rect(self.ecran, color, rect)
        pg.display.update()
