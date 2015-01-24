#importing necessary modules and starting up python
import random
import time
import pygame
import sys
from pygame.locals import *
pygame.init()

#initialising variables needed and drawing the window
size = [1280, 720]
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED =(255,0,0)
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

#defining the functions to draw lines and diamonds on the screen
def line(coods1, coods2):
        print pygame.draw.lines(screen, RED, False,[coods1,coods2], 5)

def drawDiamond(x,y,n,colour):
    pygame.draw.polygon(screen, colour,[[x,y],[x+n,y+n],[x, y+2*n],[x-n,y+n]])

def drawScreen():
    line1 = line((154, 137),(80, 265))
    line2 = line ((80,265),(280,265))
    line3 = line((150,140),(280,265))
    line4 = line((280,265),(170,385))
    line5 = line((80,265),(170,385))
    line6 = line((170,385),(100,505))
    line7 = line((100,505),(300,505))
    line8 = line((300,505),(400,380))
    line9 = line((280,265),(400,380))
    line10 = line((300,505),(540,505))
    line11 =line((400,380),(540,505))
    line12 =line((400,380),(500,260))
    line13 =line((540,505),(700,380))
    line14 =line((750,265),(700,380))
    line15 = line((500,260),(750,260))
    line16 = line((540,505),(800,505))
    line17 = line((800,505),(700,380))

    diamond1 = drawDiamond(150,130,15,BLACK)
    diamond2 = drawDiamond(80,250,15,BLACK)
    diamond3 = drawDiamond(280,250,15,BLACK)
    diamond4 = drawDiamond(170,370,15,BLACK)
    diamond5 = drawDiamond(100,490,15,BLACK)
    diamond6 = drawDiamond(300,490,15,BLACK)
    diamond7 = drawDiamond(400,370,15,BLACK)
    diamond8 = drawDiamond(540,490,15,BLACK)
    diamond9 = drawDiamond(500,250,15,BLACK)
    diamond10 = drawDiamond(750,250,15,BLACK)
    diamond11 = drawDiamond(800,490,15,BLACK)
    diamond12 = drawDiamond(700,370,15,BLACK)


def spawn():
    rspawn = random.randint(0,3)
    tspawn = random.randint(0,3)
    global treasure
    if tspawn == 0:
         treasure = 't'
    elif tspawn == 1:
        treasure = 'a'
    elif tspawn == 2:
        treasure = 'e'
    elif tspawn ==3:
        treasure = 'g'
    global rstart
    if rspawn == 0:
        rstart = 'c'
    elif rspawn == 1:
        rstart = 'j'
    elif rspawn == 2:
        rstart = 'd'
    elif rspawn ==3:
        rstart = 'i'
spawn()
    
"""
This code has been adapted from code taken from the site
http://geekly-yours.blogspot.co.uk/2014/03/dijkstra-algorithm-python-example-source-code-shortest-path.html

"""

def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
    """ calculates a shortest path tree routed in src
    """
    # a few sanity checks
    if src not in graph:
        raise TypeError('the root of the shortest path tree cannot be found in the graph')
    if dest not in graph:
        raise TypeError('the target of the shortest path cannot be found in the graph')    
    # ending condition
    if src == dest:
        treasureCounter.addScore(1)
        scoreCounter.addScore(30-(distances[dest]))
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
            print pred
        print('shortest path: '+str(path)+" cost="+str(distances[dest]))
            
    else :     
        # if it is the initial run, initializes the cost
        if not visited: 
            distances[src]=0
        # visit the neighbors
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # mark as visited
        
        visited.append(src)
        # now that all neighbors have been visited: recurse                         
        # select the non visited node with lowest distance 'x'
        # run Dijskstra with src='x'
        
        unvisited = {}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))
        
        x=min(unvisited, key=unvisited.get)
        
        dijkstra(graph,x,dest,visited,distances,predecessors)


"""
"""

if __name__ == "__main__":
    graph = {'t': {'a': 1, 'b': 5},
            'a': {'t': 1, 'b': 4, 'e': 2},
            'b': {'a': 4, 't': 5, 'e': 4, 'f': 6},
            'e': {'a': 2, 'b': 4, 'g': 1},
            'c': {'f': 3, 'j': 1},
            'f': {'b': 6, 'c': 3, 'g': 7, 'h': 2},
            'j': {'c': 1, 'd': 5},
            'g': {'e': 1, 'f': 7, 's': 3},
            'd': {'j': 5, 'h': 6, 'i': 3},
            's': {'g': 3, 'h': 2},
            'h': {'s': 2, 'f': 2, 'i': 4, 'd':6},
            'i': {'h': 4, 'd': 3}}

    #defining the treasure/score counter and calling the draw function
    treasureCounter = Counter(0,1160,410)
    treasureCounter.drawCounter()
    scoreCounter = Counter(0,1160,300)
    scoreCounter.drawCounter()
    drawScreen()
    dijkstra(graph,rstart,treasure , [], {}, {})
    """
    time.sleep(3)
    spawn()
    dijkstra(graph,rstart,treasure, [], {}, {})
    time.sleep(3)
    spawn()
    dijkstra(graph,rstart,treasure, [], {}, {})
    """
    #script to easily close window if it runs through
    pygame.display.update()
    raw_input("Press enter to quit")
    pygame.quit()
    
    
