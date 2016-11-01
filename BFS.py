import Queue
from commonFunctions import getNeighbours

def BFS(start, end, maze):
	"""
	Breadth-first search works by starting at the root and traversing the
	neighbour nodes before traversing the next level.

	BFS returns the path found from the start to end node.
	"""
	dimension = len(maze)

	# This will be the path taken to get to a particular node.
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
		# Pulls the item at the front of the queue
		element = explore.get()

		# Element is of the form [(x,y), [*path so far*]]
		node = element[0]
		path = element[1]

		# Appends path to node.
		path = path + [node]

		# If the node we're examining is the end node, we should return the path to this node.
		if node == end:
			return path

		# IF the node has not been visited before, we want to examine it further.
		if node not in visited[0]:
			# Gets neighbours of current node
			neighbours = getNeighbours(node,dimension)
			#For each neighbour, check to see if it's a passageway that hasn't been explored before.
			for neighbour in neighbours:
				if maze[neighbour[0]][neighbour[1]][1] == False:
					if neighbour not in visited:
						# If it's a passageway that hasn't been explored before, add it to the explore list.
						explore.put([neighbour, path])

		# Now that we've visited the current node, add it to the visited list to avoid looking at it again.
		visited.append(node)