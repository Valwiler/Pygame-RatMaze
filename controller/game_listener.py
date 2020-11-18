import sys
import pygame


class Game_Listener:
    def __init__(self):
        self.pressed_up = False
        self.pressed_down = False
        self.pressed_left = False
        self.pressed_right = False

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    self.pressed_left = True
                elif event.key == pygame.K_RIGHT:
                    self.pressed_right = True
                elif event.key == pygame.K_UP:
                    self.pressed_up = True
                elif event.key == pygame.K_DOWN:
                    self.pressed_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.pressed_left = False
                elif event.key == pygame.K_RIGHT:
                    self.pressed_right = False
                elif event.key == pygame.K_UP:
                    self.pressed_up = False
                elif event.key == pygame.K_DOWN:
                    self.pressed_down = False
        return self.pressed_up, self.pressed_down, self.pressed_left, self.pressed_right
