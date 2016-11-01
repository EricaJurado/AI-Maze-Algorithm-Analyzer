from primMazeGen import Prim
from aStar import aStar
from UniformCostDijkstra import UniformCostDijkstra
from timeit import default_timer
from timer import algorithm_timer
from BFS import BFS
from DFS import DFS
from Stats import median
from Stats import mean
import csv

def Main(startSize, endSize, jumpSize):
    """
    this function generates the actual maze and 
    then runs each of the algorithms through the maze
    """
    mazeInfo = Prim(startSize)
    start = mazeInfo[0]
    end = mazeInfo[1]
    maze = mazeInfo[2]

    total_time_aStar = algorithm_timer(aStar,start,end,maze)
    total_time_dijksta = algorithm_timer(UniformCostDijkstra, start, end, maze)
    total_time_BFS = algorithm_timer(BFS, start, end, maze)
    total_time_DFS = algorithm_timer(DFS, start, end, maze)

    total_times = []

    total_times.append(total_time_aStar) 
    total_times.append(total_time_dijksta) 
    total_times.append(total_time_BFS)
    total_times.append(total_time_DFS)

    return(total_times)


#these are the only variables that would
#ever need to be changed when running this code
startSize = 5
endSize = 20
jumpSize = 5 
i=0


#the following bunches of lists are used for 
#statistics and CSV outputs
aStar_raw_data = []   
BFS_raw_data = []
DFS_raw_data = []
UniformCostDijkstra_raw_data = []

aStar_Stats = []
UniformCostDijkstra_Stats = []
BFS_Stats = []
DFS_Stats = []

aStar_Stats_clean = []
UniformCostDijkstra_Stats_clean = []
BFS_Stats_clean = []
DFS_Stats_clean = []



#this is the main loop that runs the entire program
while startSize <= endSize:
    while i < 20:
        total_times = Main(startSize,endSize,jumpSize)
        aStar_raw_data.append(["aStar", startSize, i, total_times[0]])
        aStar_Stats.append(total_times[0])
        
        UniformCostDijkstra_raw_data.append(["Dijkstra", startSize, i, total_times[1]])
        UniformCostDijkstra_Stats.append(total_times[1])
        
        BFS_raw_data.append(["BFS", startSize, i, total_times[2]])
        BFS_Stats.append(total_times[2])
        
        DFS_raw_data.append(["DFS", startSize, i, total_times[2]])
        DFS_Stats.append(total_times[3])

        i+=1
    i=0  

    
    #this is to sort all of the lists of times for median calculations
    aStar_Stats.sort()
    UniformCostDijkstra_Stats.sort()
    BFS_Stats.sort()
    DFS_Stats.sort()


    #this is where the statistics are calculated 
    #the mean and median functions are helper functions in the stat file
    aStar_Stats_clean.append([startSize, "aStar", mean(aStar_Stats), median(aStar_Stats)])
    UniformCostDijkstra_Stats_clean.append([startSize, "Dijkstra", mean(UniformCostDijkstra_Stats), median(UniformCostDijkstra_Stats)])
    BFS_Stats_clean.append([startSize, "BFS", mean(BFS_Stats), median(BFS_Stats)])
    DFS_Stats_clean.append([startSize, "DFS", mean(DFS_Stats), median(DFS_Stats)])



    with open("clean_data.csv", "ab") as fi:
        writer = csv.writer(fi, delimiter= ",", lineterminator = "\n")
        writer.writerows(aStar_Stats_clean)
        writer.writerows(UniformCostDijkstra_Stats_clean)
        writer.writerows(BFS_Stats_clean)
        writer.writerows(DFS_Stats_clean)


        
    with open("raw_data_file.csv", "ab") as f:
        writer = csv.writer(f, delimiter= ",", lineterminator = "\n")
        writer.writerows(aStar_raw_data)
        writer.writerows(UniformCostDijkstra_raw_data)
        writer.writerows(BFS_raw_data)
        writer.writerows(DFS_raw_data)

    aStar_raw_data = []   
    BFS_raw_data = []
    DFS_raw_data = []
    UniformCostDijkstra_raw_data = []

    aStar_Stats = []
    BFS_Stats = []
    DFS_Stats = []
    UniformCostDijkstra_Stats = []

    aStar_Stats_clean = []
    UniformCostDijkstra_Stats_clean = []
    BFS_Stats_clean = []
    DFS_Stats_clean = []
    
    startSize += jumpSize

    fi.close()
    f.close()










