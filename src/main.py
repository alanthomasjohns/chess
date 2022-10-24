import pygame
import sys

from const import *
from game import *



class Main:
    def __init__(self):
        pygame.init() #initialized the pygame module
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #created a pygame screen of our defined height and width
        pygame.display.set_caption('Chess') #name of application
        self.game = Game()

    def mainloop(self):

        game = self.game
        screen = self.screen #created variable to avoid calling self.thing each time

        while True:
            game.show_bg(screen)
            game.show_pieces(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update() #updates the screen


main = Main()
main.mainloop()