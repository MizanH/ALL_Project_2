import random
import pygame
from pygame.locals import *
import sys
import time
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
        scoreCounter.addScore(15-(distances[dest]))
        #run the respawning script here
        # We build the shortest path and display it
        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
            print pred
        print('shortest path: '+str(path)+" cost="+str(distances[dest]))
        path =[]
          
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
            'h': {'s': 2, 'f': 2, 'i': 4},
            'i': {'h': 4, 'd': 3}}
    print 'treasure ' + treasure
    print 'start ' + rstart
    
    dijkstra(graph,rstart,treasure)
    time.sleep(3)

#script to easily close window if it runs through
pygame.display.update()
raw_input("Press enter to quit")
pygame.quit()
    
    
