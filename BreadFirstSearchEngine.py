from AbstractSearchEngine import AbstractSearchEngine
from LocationQueue import LocationQueue
class BreadFirstSearchEngine(AbstractSearchEngine):

    def __init__(self,width,height):
        super().__init__(width,height)
        self.doSearchOn2DGrid()


    def doSearchOn2DGrid(self):
        width = self.maze.getWidth()
        height = self.maze.getHeight()
        alreadyVisitedFlag = {}
        predecessor = {}
        queue = LocationQueue(400)

        
        for i in range(0,width):
            temp=[]
            temp2=[]
            for _ in range(0,height):
                temp.append(False)
                temp2.append(None)

            alreadyVisitedFlag[i] = temp
            predecessor[i] = temp2

        alreadyVisitedFlag[self.startLoc.x][self.startLoc.y] = True
        queue.addToBackOfQueue(self.startLoc)
        success = False

        while(queue.isEmpty() == False):
            
            head = queue.peekAtFrontOfQueue()
            if(head == None):
                break
            connected = self.getPossibleMoves(head)
            for i in range(0,4):
                if(connected[i] == None):
                    break
                w = connected[i].x
                h = connected[i].y
                if(alreadyVisitedFlag[w][h] == False):
                    
                    alreadyVisitedFlag[w][h] = True
                    predecessor[w][h] = head
                    queue.addToBackOfQueue(connected[i])
                    
                    if(self.equals(connected[i],self.goalLoc)):    
                        
                        success = True
                        break
            if(success):
                break
        
            
            queue.removeFromFrontOfQueue()

        self.maxDepth = 0
        if(success):
            self.searchPath[self.maxDepth] = self.goalLoc
            self.maxDepth = self.maxDepth + 1
            for i in range(0,100):
                self.searchPath[self.maxDepth] = predecessor[self.searchPath[self.maxDepth - 1].x][self.searchPath[self.maxDepth - 1].y]
                self.maxDepth = self.maxDepth + 1
                if(self.searchPath[self.maxDepth - 1] == self.startLoc):
                    break            