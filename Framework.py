from primMazeGen import Prim
from aStar import aStar
from UniformCostDijkstra import UniformCostDijkstra

def Main(startSize, endSize, jumpSize):

    #while (startSize < endSize):
    #	startSize += jumpSize
    mazeInfo = Prim(startSize)
    start = mazeInfo[0]
    end = mazeInfo[1]
    maze = mazeInfo[2]
    aStar(start,end,maze)
    UniformCostDijkstra(start, end, maze)

Main(5, 5, 0)
