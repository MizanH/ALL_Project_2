import pygame
import time
from random import randint

pygame.init()
# Need to define a colour before using a colour
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
YELLOW =(255,  255,  0)

size = [600, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Traffic Light")

done= False
clock = pygame.time.Clock()
# Defining the states of the traffic 
a = randint(2000, 10000)

# Defining the states of the traffic
def Green():
    pygame.draw.rect(screen, BLACK, [200, 100, 100, 300])
    pygame.draw.circle(screen, GREEN, [250, 350], 40)
    pygame.draw.circle(screen, YELLOW, [250, 250], 40, 2)
    pygame.draw.circle(screen, RED, [250, 150], 40, 2)
    return;

def Amber():
    pygame.draw.rect(screen, BLACK, [200, 100, 100, 300])
    pygame.draw.circle(screen, YELLOW, [250, 250], 40)
    pygame.draw.circle(screen, GREEN, [250, 350], 40, 2)
    pygame.draw.circle(screen, RED, [250, 150], 40, 2)
    return;

def Red():
    pygame.draw.rect(screen, BLACK, [200, 100, 100, 300])
    pygame.draw.circle(screen, RED, [250, 150], 40)
    pygame.draw.circle(screen, GREEN, [250, 350], 40, 2)
    pygame.draw.circle(screen, YELLOW, [250, 250], 40, 2)
    return;

while not done:
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
# Actual traffic light code
    screen.fill(WHITE)
    Green()
    pygame.display.flip()
    pygame.time.wait(a)
    screen.fill(WHITE)
    Amber()
    pygame.display.flip()
    pygame.time.wait(2000)
    screen.fill(WHITE)
    Red()
    pygame.display.flip()
    pygame.time.wait(3500)
