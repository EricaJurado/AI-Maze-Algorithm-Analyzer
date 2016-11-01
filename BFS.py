import Queue
from commonFunctions import getNeighbours

def BFS(start, end, maze):
	dimension = len(maze)
	path = []
	# This queue will hold the nodes to be explored.
	# Since it's BFS it will be the most recent children. 
	explore = Queue.Queue()
	explore.put([start, path])

	# Will hold the visited nodes so no node will be visited more than once.
	visited = []
	visited.append(start)
	
	# While there are nodes to continue examining
	while explore.empty() == False:
		element = explore.get()
		node = element[0]
		path = element[1]

		path = path + [node]

		if node == end:
			return path

		if node not in visited[0]:
			neighbours = getNeighbours(node,dimension)
			for neighbour in neighbours:
				if maze[neighbour[0]][neighbour[1]][1] == False:
					if neighbour not in visited:
						explore.put([neighbour, path])

		visited.append(node)