class LocationQueue():
    def __init__(self,num):
        self.queue = []
        self.head = self.tail = 0
        self.len = num

    def addToBackOfQueue(self,n):
        self.queue.append(n)
        if(self.tail >= (self.len-1)):
            self.tail = 0
        else:
            self.tail = self.tail + 1

    def removeFromFrontOfQueue(self):
        ret = self.queue[self.head]
        if(self.head >= (self.len-1)):
            self.head = 0
        else:
            self.head = self.head + 1
        return ret               

    def isEmpty(self):
        return self.head == (self.tail+1)

    def peekAtFrontOfQueue(self):
        try:
            return self.queue[self.head]
        except:
            return None
        
        
    


