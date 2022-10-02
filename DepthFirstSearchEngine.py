from AbstractSearchEngine import AbstractSearchEngine
class DepthFirstSearchEngine(AbstractSearchEngine):
    def __init__(self,width,height):
        super().__init__(width,height)
        self.iterateSearch(self.startLoc, 1)

    def iterateSearch(self,loc,depth):
        if(self.isSearching == False):
            return
        
        self.maze.setValue(loc.x,loc.y,depth)
        moves = self.getPossibleMoves(loc)
        
        for i in range(0,4):
            if(moves[i] == None):
                break    
            self.searchPath[depth] = moves[i]
            if(self.equals(moves[i],self.goalLoc)):
                print("Found the goal at ", moves[i].x ,", " , moves[i].y)
                self.isSearching = False
                self.maxDepth = depth
                print(self.maxDepth)
                return
            else:
                self.iterateSearch(moves[i],depth+1)
                if(self.isSearching == False):
                    return
                     
                        
