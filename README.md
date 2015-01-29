ALL_Project_2
=============
Treasure Hunt
-------------
The aim of this project is to creat a Robot that will find its own way from location to location.
While the robot is moving between the locations it must follow a set of traffic light instructions.
It cannot move while the light is red, while amber it is slowing down, and wheen it is green it can move at full speed.
Treause is hidden at one of these locations and once the robot goes to this location score will be given.
Once the robot has gotten to the first treasure another one will spawn at another location/.
The robot then has to move and find that, this repeats for a set amount of time.

-------------

Pathfinding
-------------
We have used Dijkstra's algorith as our form of pathfinding.
This is becasue this allows us to add costs to the connections between the locations.
This means that our program takes the quickest path over the shortest path.

-------------

Traffic lights
-------------
The traffic lights work on a random number generation system.
each time the robot moves there is a 1 in 100 chance that the traffic light will turn amber.
If the ight has turned amber ther robot will move 3X slower for the next 30 ticks of the program.
Once the 30 ticks have passed the light changes to red and the program stops for 3 seconds.
When the 3 seconds are over then the light changes back to green and the robot moves at full speed.

-------------

Scoring System
-------------
The scoring system in the game is based on the costs of the edges between nodes. Whenever the robot
reaches the treasure, they gain 30 score, minus the cost of the sum of all paths the robot travelled
on to reach the treasure. Each treasure collected also increases the treasure counter by 1, so that the
user can track how many treasures they have collected
