from primMazeGen import Prim
from aStar import aStar

def Main(startSize, endSize, jumpSize):

    #while (startSize < endSize):
    #	startSize += jumpSize
    mazeInfo = Prim(startSize)
    start = mazeInfo[0]
    end = mazeInfo[1]
    maze = mazeInfo[2]
    print maze
    print start
    print end
    aStar(start,end,maze)

Main(4, 4, 0)
