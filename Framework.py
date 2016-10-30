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
    #aStar(start,end,maze)
    result = UniformCostDijkstra(start, end, maze)
    print result

Main(4, 4, 0)
