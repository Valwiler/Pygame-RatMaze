import sys

import pygame
import view.Window
import time


class GameListener():

    def __init__(self):
        self.pressed_up = False

        self.pressed_down = False

        self.pressed_left = False

        self.pressed_right = False

    def get_input(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # check for key presses
                if event.key == pygame.K_LEFT:  # left arrow turns left
                    self.pressed_left = True
                elif event.key == pygame.K_RIGHT:  # right arrow turns right
                    self.pressed_right = True
                elif event.key == pygame.K_UP:  # up arrow goes up
                    self.pressed_up = True
                elif event.key == pygame.K_DOWN:  # down arrow goes down
                    self.pressed_down = True
            elif event.type == pygame.KEYUP:  # check for key releases
                if event.key == pygame.K_LEFT:  # left arrow turns left
                    self.pressed_left = False
                elif event.key == pygame.K_RIGHT:  # right arrow turns right
                    self.pressed_right = False
                elif event.key == pygame.K_UP:  # up arrow goes up
                    self.pressed_up = False
                elif event.key == pygame.K_DOWN:  # down arrow goes down
                    self.pressed_down = False
        return self.pressed_up, self.pressed_down, self.pressed_left, self.pressed_right
