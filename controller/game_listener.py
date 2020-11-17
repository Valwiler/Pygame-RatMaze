import sys

import pygame


class Game_Listener:
    @staticmethod
    def get_input():
        pressed_up = False
        pressed_down = False
        pressed_left = False
        pressed_right = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    pressed_left = True
                elif event.key == pygame.K_RIGHT:
                    pressed_right = True
                elif event.key == pygame.K_UP:
                    pressed_up = True
                elif event.key == pygame.K_DOWN:
                    pressed_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    pressed_left = False
                elif event.key == pygame.K_RIGHT:
                    pressed_right = False
                elif event.key == pygame.K_UP:
                    pressed_up = False
                elif event.key == pygame.K_DOWN:
                    pressed_down = False
        return pressed_up, pressed_down, pressed_left, pressed_right
    # @staticmethod
    # def get_input():
    #
    #     x_move = 0
    #     y_move = 0
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #         elif event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_ESCAPE:
    #                 sys.exit()
    #             if event.key == pygame.K_LEFT:
    #                 x_move = -1
    #             elif event.key == pygame.K_RIGHT:
    #                 x_move = 1
    #             elif event.key == pygame.K_UP:
    #                 y_move = -1
    #             elif event.key == pygame.K_DOWN:
    #                 y_move = 1
    #             else:
    #                 x_move, y_move = 0,0
    #
    #    move = (x_move, y_move)
    #    return move
