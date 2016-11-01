from primMazeGen import Prim
from aStar import aStar
from UniformCostDijkstra import UniformCostDijkstra
from timeit import default_timer
from timer import algorithm_timer

def Main(startSize, endSize, jumpSize):

    #while (startSize < endSize):
    #	startSize += jumpSize
    mazeInfo = Prim(startSize)
    start = mazeInfo[0]
    end = mazeInfo[1]
    maze = mazeInfo[2]

    print algorithm_timer(aStar,start,end,maze)
    

    #path = UniformCostDijkstra(start,end,maze)


Main(60, 60, 0)
