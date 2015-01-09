import pygame
pygame.init()

size = [1280, 720]
WHITE = (255,255,255)
BLACK = (0,0,0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Test Window')
screen.fill(WHITE)

pygame.display.flip()



class Counter():
    def __init__(self, score, x, y):
        self.score = score
        self.x = x
        self.y = y

    def drawCounter(self):
        pygame.draw.rect(screen, BLACK, (self.x,self.y,300,100), 5)
        

treasureCounter = Counter("test",960,410)
treasureCounter.drawCounter()
pygame.display.update()

scoreCounter = Counter("test",960,300)
scoreCounter.drawCounter()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
