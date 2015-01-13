import pygame
import sys
pygame.init()

size = [1280, 720]
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Test Window')
screen.fill(WHITE)

pygame.display.flip()

def drawDiamond(x,y,n,colour):
    pygame.draw.polygon(screen, colour,[[x,y],[x+n,y+n],[x, y+2*n],[x-n,y+n]])

diamond1 = drawDiamond(50,50,25,BLACK)
diamond2 = drawDiamond(600,300,50,BLUE)

#Formula to create a diamond from any x+y coordinate
#(x,y),(x+n,y+n),(x, y+2n),(x-n,y+n)

pygame.display.update()
raw_input("Press enter to quit")
pygame.quit()
