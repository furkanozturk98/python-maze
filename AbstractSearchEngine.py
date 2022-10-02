from Location import Location
from Maze import Maze
class AbstractSearchEngine(object):

    searchPath = []
    currentLoc = None
    maxDepth = 0
    pathCount = 0
    isSearching = True
    def __init__(self,width,height):
        self.maze = Maze(width,height)
        self.initSearch()
    def getMaze(self):
        return self.maze   
    def initSearch(self):
        if(not self.searchPath ):
            for _ in range(0,1000):
                self.searchPath.append(Location(None,None))
        self.startLoc = self.maze.startLoc
        self.currentLoc = self.startLoc
        self.goalLoc = self.maze.goalLoc
        self.searchPath[self.pathCount] = self.currentLoc
        self.pathCount = self.pathCount +1

    def equals(self,d1,d2):
        return d1.x == d2.x and d1.y == d2.y

    def getPath(self):
        print("maxDepth: ",self.maxDepth)
        ret = []
        for i in range(0,self.maxDepth):
            ret.append(self.searchPath[i])
        return ret

    def getPossibleMoves(self,loc):
        tempMoves = [None,None,None,None]     
        x = loc.x
        y = loc.y
        num = 0 
        if(self.maze.getValue(x-1,y) == 0 or self.maze.getValue(x-1,y) == Maze.GOAL_LOC_VALUE): 
            tempMoves[num] = Location(x-1,y)
            num = num + 1   
        if(self.maze.getValue(x+1,y) == 0 or self.maze.getValue(x+1,y) == Maze.GOAL_LOC_VALUE):
            tempMoves[num] = Location(x+1,y)
            num = num + 1
        if(self.maze.getValue(x,y-1) == 0 or self.maze.getValue(x,y-1) == Maze.GOAL_LOC_VALUE):
            tempMoves[num] = Location(x,y-1)
            num = num + 1
        if(self.maze.getValue(x,y+1) == 0 or self.maze.getValue(x,y+1) == Maze.GOAL_LOC_VALUE):
            tempMoves[num] = Location(x,y+1)
            num = num + 1  
        return tempMoves             