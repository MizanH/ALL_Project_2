#importing necessary modules and starting up python
import pygame
import sys
from pygame.locals import *
pygame.init()

#initialising variables needed and drawing the window
size = [1280, 720]
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
font = pygame.font.SysFont(None, 48)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Test Window')
screen.fill(WHITE)
screen.blit(font.render("Score", True, BLACK),(1060,330))
screen.blit(font.render("Treasures", True, BLACK),(990,450))
pygame.display.update()
pygame.display.flip()

#defining the class for the treasure/score counter
class Counter():
    def __init__(self, score, x, y):
        self.score = score
        self.x = x
        self.y = y

    #function used to draw the initial score and text box
    def drawCounter(self):
        pygame.draw.rect(screen, BLACK, (self.x,self.y,100,100), 5)
        screen.blit(font.render(str(self.score), True, BLACK),
                    (self.x+30, self.y+35))
        pygame.display.update()

    #function to draw the score when the treasure is collected
    #also sets score to new score
    def addScore(self, addScore):

        pygame.draw.rect(screen, WHITE, (self.x+30, self.y+35,50,50))
        screen.blit(font.render(str(self.score+addScore), True, BLACK),
                    (self.x+30, self.y+35))
        self.score = self.score+addScore
        pygame.display.update()

#defining the treasure/score counter and calling the draw function
treasureCounter = Counter(0,1160,410)
treasureCounter.drawCounter()
scoreCounter = Counter(0,1160,300)
scoreCounter.drawCounter()

#calculating the addition to treasure/score counter
#if positionOfRobot == positionOfTreasure:
    #treasureCounter.addScore(1)
    #scoreCounter.addScore(15-(costOfPathTaken))
    #run the respawning script here




#script to easily close window if it runs through
pygame.display.update()
raw_input("Press enter to quit")
pygame.quit()
