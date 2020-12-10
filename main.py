import pygame
import model.game as g
import cProfile



def main():
    pygame.init()
    pygame.display.set_caption('Laborat')
    game = g.Game()
    game.run()
    pygame.quit()


if __name__ == '__main__':
   exit(main())
