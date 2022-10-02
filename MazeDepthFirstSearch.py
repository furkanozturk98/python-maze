import tkinter as tk
from Maze import Maze
from DepthFirstSearchEngine import DepthFirstSearchEngine
class MazeDepthFirstSearch():
    currentSearchEngine = None
    def __init__(self):
        self.currentSearchEngine = DepthFirstSearchEngine(10,10)
    def paint(self):
        if (self.currentSearchEngine == None):
            return
        maze = self.currentSearchEngine.getMaze()
        width = maze.getWidth()
        height = maze.getHeight()
        print("Size of current maze: ", width , " by ", height)
        my_window = tk.Tk()
        my_window.geometry('350x350')
        canvas = tk.Canvas(my_window, width = 300, height = 300, bg = "white")
        canvas.pack()
        labels = {}
        for i in range(0,width):
            TempList = []
            mylabel = None
            for j in range(0,height):   
                value = maze.getValue(i,j)        
                if(value == Maze.OBSTICLE):
                    canvas.create_rectangle(0+(j*30),0+(i*30),30+(j*30), 30+(i*30),fill="grey")
                    mylabel = canvas.create_text(15+(j*30),15+(i*30), fill="black",font="Times 10",text="")
                elif(value == Maze.START_LOC_VALUE or value == 1):
                    canvas.create_rectangle(0+(j*30),0+(i*30),30+(j*30), 30+(i*30))
                    mylabel = canvas.create_text(15+(j*30),15+(i*30),fill="blue",font="Times 10",text="S")
                elif(value == Maze.GOAL_LOC_VALUE or value == -3):
                    canvas.create_rectangle(0+(j*30),0+(i*30),30+(j*30), 30+(i*30))
                    mylabel = canvas.create_text(15+(j*30),15+(i*30),fill="red",font="Times 10",text="G")
                else:
                    canvas.create_rectangle(0+(j*30),0+(i*30),30+(j*30), 30+(i*30))
                    mylabel = canvas.create_text(15+(j*30),15+(i*30), fill="black",font="Times 10",text="")
                TempList.append(mylabel)
            labels[i] = TempList     
        path = self.currentSearchEngine.getPath()
        for i in range(1,len(path)):
            x = path[i].x
            y = path[i].y
            value = maze.getValue(x,y)
            canvas.itemconfig(labels[x][y], text = str(value) ) 
        canvas.grid(padx=20,pady=20)
        my_window.mainloop()       
search = MazeDepthFirstSearch()
search.paint()                    


