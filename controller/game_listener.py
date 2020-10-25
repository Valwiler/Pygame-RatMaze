import sys

import pygame
import view.Window
import time

class GameListener():


    def __init__(self, laborat, SCREEN_WIDTH, SCREEN_HEIGHT, MVT):
        self.laborat = laborat
        self.scren_w = SCREEN_WIDTH
        self.screen_h = SCREEN_HEIGHT
        self.mvt = MVT


    def get_input(self):
       # Window.update_icons()
        pressed_up = False
        pressed_down = False
        pressed_left = False
        pressed_right = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # check for key presses
                if event.key == pygame.K_LEFT:  # left arrow turns left
                    pressed_left = True
                elif event.key == pygame.K_RIGHT:  # right arrow turns right
                    pressed_right = True
                elif event.key == pygame.K_UP:  # up arrow goes up
                    pressed_up = True
                elif event.key == pygame.K_DOWN:  # down arrow goes down
                    pressed_down = True
            elif event.type == pygame.KEYUP:  # check for key releases
                if event.key == pygame.K_LEFT:  # left arrow turns left
                    pressed_left = False
                elif event.key == pygame.K_RIGHT:  # right arrow turns right
                    pressed_right = False
                elif event.key == pygame.K_UP:  # up arrow goes up
                    pressed_up = False
                elif event.key == pygame.K_DOWN:  # down arrow goes down
                    pressed_down = False
        return pressed_up,pressed_down,pressed_left,pressed_right

        # In your game loop, check for key states:

        Window.update_icons()

        #for events in pygame.event.get():
        #    Window.update_icons()
        #    temp_laborat_position = self.laborat.get_position()
        #    keyPressed = False
        #    key = pygame.key.get_pressed()
        #    #print(key)
        #    if events.type == pygame.KEYDOWN:
        #        keyPressed = True
        #        while keyPressed is True:
        #            if key[pygame.K_RIGHT]:
        #                self.laborat.position[0] += self.mvt
        #                print('right')
        #            if key[pygame.K_LEFT]:
        #                self.laborat.position[0] -= self.mvt
        #                print('left')
        #            if key[pygame.K_DOWN]:
        #                self.laborat.position[1] += self.mvt
        #                print('down')
        #            if key[pygame.K_UP]:
        #                self.laborat.position[1] -= self.mvt
        #                print('up')
        #
        #
        ##print(str(temp_laborat_position[0]) + " " + str(temp_laborat_position[1]))
        #            self.new_position_validation()
        #            time.sleep(0.1)
        #    elif events.type == pygame.KEYUP :
        #        keyPressed = False
        #        break
        #
        #
        #
        #
       #for evenement in pygame.event.get():
       #  temp_laborat_position = self.laborat.get_position()
       #  if evenement.type == pygame.QUIT:
       #      self.game.running = False   #TODO: arreter le jeu sans erreur a la fin
       #      break
       #  elif evenement.type == pygame.KEYDOWN:  #TODO: deplacer en continu et pas a la pression (voir pygame.KEYUP)
       #      if evenement.key == pygame.K_RIGHT:
       #          self.laborat.position[0] += self.mvt
       #      elif evenement.key == pygame.K_LEFT:
       #          self.laborat.position[0] -= self.mvt
       #      elif evenement.key == pygame.K_DOWN:
       #          self.laborat.position[1] += self.mvt
       #      elif evenement.key == pygame.K_UP:
       #          self.laborat.position[1] -= self.mvt
       #
       #  print(str(temp_laborat_position[0]) + " " + str(temp_laborat_position[1]))
       #  self.new_position_validation()
       #  Window.update_icons()




