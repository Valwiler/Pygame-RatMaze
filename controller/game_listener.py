import sys

import pygame


class Game_Listener:

    def get_input():
        x_move = 0
        y_move = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    x_move = -1
                elif event.key == pygame.K_RIGHT:
                    x_move = 1
                elif event.key == pygame.K_UP:
                    y_move = -1
                elif event.key == pygame.K_DOWN:
                    y_move = 1

        move = (x_move, y_move)
        return move
        #return x_move, y_move