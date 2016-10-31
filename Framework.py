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
    path = aStar(start,end,maze)
    # print path
    path = UniformCostDijkstra(start,end,maze)
    # print path

Main(5, 5, 0)
