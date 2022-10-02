from Location import Location
import random
class Maze:
    OBSTICLE = -1
    START_LOC_VALUE = -2
    GOAL_LOC_VALUE = -3
    width = 0
    height = 0
    startLoc = Location(None,None)
    goalLoc  = Location(None,None)

    maze = {}

    def __init__(self,width,height):
        print("New maze of size ", width , " by " , height)
        self.width = width
        self.height = height
        for i in range(0,width+2):
            Temp = []
            for _ in range(0,height+2):
                Temp.append(0)

            self.maze[i] = Temp
        for i in range(0,height+2):
            self.maze[0][i] = self.maze[width+1][i] = self.OBSTICLE 
        for i in range(0,width+2):
            self.maze[i][0] = self.maze[i][height+1] = self.OBSTICLE           

        max_obsticles = (width * height) / 3
        for i in range(0,int(max_obsticles)):
            x =  int(random.random() * width)
            y =  int(random.random() * height)
            self.setValue(x,y,self.OBSTICLE)

        self.startLoc.x = 0
        self.startLoc.y = 0
        self.setValue(0,0,0)

        self.goalLoc.x = width - 1 
        self.goalLoc.y = height - 1
        self.setValue(width - 1, height - 1, self.GOAL_LOC_VALUE )

    def getValue(self,x, y):
        return self.maze[x+1][y+1]
    def setValue(self, x,  y,  value):
        self.maze[x+1][y+1] = value

    def  getWidth(self):
         return self.width
    def  getHeight(self):
        return self.height  