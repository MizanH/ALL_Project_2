import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280,720))
print screen;

pygame.display.update()
colorName=("red","green","blue")
listOfColors=(0,255,0)
screen.fill(listOfColors)

red=(255,0,0)
pygame.draw.lines(screen, red, False ,[(100,100),(150,200),(200,100)],5)
'''
class shapes:
    line1=0
    line2=0
    line3=0
    line4=0
    coods1 = (0, 0)
    coods2 = (0, 0)
    
    def ___init__(self, coods1, coods2):
        self.coods1 = coods1
        self.coods2 = coods2
    
    def printline1(self):
        print pygame.draw.lines(screen, red, False,[(100,300),(150,200),(200,100)],5)
    def printline2(self):
        print pygame.draw.lines(screen, red, False ,[(300,200),(150,200),(200,100)],5)
    def printline3(self):
        print pygame.draw.lines(screen, red, False ,[(100,300),(150,200),(400,100)],5)
    def printline4(self):
        print pygame.draw.lines(screen, red, False ,[(400,100),(150,200),(300,100)],5)
firstshape = shapes()
firstshape.printline1()
firstshape.printline2()
firstshape.printline3()
firstshape.printline4()
pygame.display.update()
'''
def line(coods1, coods2):
        print pygame.draw.lines(screen, red, False,[coods1,coods2], 5)

testline = line((0, 100),(200, 300))

testline2 = line((300,400),(640, 480))
pygame.display.update()
