import pygame
import time
pygame.init()
screen = pygame.display.set_mode((600,400))
print screen;
colour = (255,255,255)
screen.fill(colour)
pygame.display.update()

ax = 20
ay = 30
red= (255,0,0)


pygame.display.update()




def movement(destx, desty,):
    bx,by=(destx,desty)
    steps_number = max( abs(bx-ax), abs(by-ay) )
    stepx = float(bx-ax)/steps_number
    stepy = float(by-ay)/steps_number
    
    for i in range(steps_number+1):
        currentx = ax + stepx*i
        currenty = ay + stepy*i
        global currentx
        global currenty
        print int(ax + stepx*i), int(ay + stepy*i)
        screen.fill(colour)
        rectangle = pygame.draw.rect(screen, red,(currentx,currenty, 25,  25 ))
    
        time.sleep(0.1)
        pygame.display.update()
movement(40, 100)
print currentx
print currenty
ax = int(currentx)
ay = int(currenty)
movement(200, 50)

pygame.display.update()
