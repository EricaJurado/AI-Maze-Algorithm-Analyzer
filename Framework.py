from primMazeGen import Prim
from aStar import aStar
from UniformCostDijkstra import UniformCostDijkstra
from timeit import default_timer
from timer import algorithm_timer
from BFS import BFS
import csv

def Main(startSize, endSize, jumpSize):
    mazeInfo = Prim(startSize)
    start = mazeInfo[0]
    end = mazeInfo[1]
    maze = mazeInfo[2]

    total_time_aStar = algorithm_timer(aStar,start,end,maze)
    

    total_time_dijksta = algorithm_timer(UniformCostDijkstra, start, end, maze)
    

    total_time_BFS = algorithm_timer(BFS, start, end, maze)

    total_times = []

    total_times.append(total_time_aStar) 
    total_times.append(total_time_dijksta) 
    total_times.append(total_time_BFS)

    return(total_times)

startSize = 5
endSize = 20
jumpSize = 5 
i=0
aStar_raw_data = []   
BFS_raw_data = []
UniformCostDijkstra_raw_data = []


while startSize <= endSize:
    while i < 20:
        total_times = Main(startSize,endSize,jumpSize)
        aStar_raw_data.append(["aStar", startSize, i, total_times[0]])
        UniformCostDijkstra_raw_data.append(["Dijkstra", startSize, i, total_times[1]])
        BFS_raw_data.append(["BFS", startSize, i, total_times[2]])

        i+=1
    i=0  

    
    #stats here

    with open("raw_data_file.csv", "ab") as f:
        writer = csv.writer(f, delimiter= ",", lineterminator = "\n")
        writer.writerows(aStar_raw_data)
        writer.writerows(UniformCostDijkstra_raw_data)
        writer.writerows(BFS_raw_data)

    aStar_raw_data = []   
    BFS_raw_data = []
    UniformCostDijkstra_raw_data = []
    
    startSize += jumpSize

    f.close()










