import pygame, sys
from pygame.locals import *

FPS = 10
#  Grid size
Window_Width = 270
Window_height = 270

White = (255, 255, 255)

#  Initiates the display, sets the title, sets the FPS clock
def main():
    global FPS_Clock, Display
    pygame.init()
    FPS_Clock = pygame.time.Clock()
    Display = pygame.display.set_mode(Window_Width, Window_height)
    pygame.display.set_caption('Sudoku GUI Solver')

    Display.fill(White)
#  Keeps the game running until a quit out
#  Updates the FPS
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPS_Clock.tick(FPS)

    if __name__=='__main__':
        main()
