from commonFunctions import getNeighbours

def DFS(start,end,maze):
	"""
	Depth-first search traverses the tree by starting at a root
	and exploring as far as possible on a branch before backtracking.

	This DFS function uses a helper function, Traversal to do this.

	DFS returns the path it found.
	"""
	dimension = len(maze)

	# This will be the path taken to get to a node.
	path = []

	# Will contain nodes that are evaulated.
	visited = []

	# Starting node and corresponding null path.
	node = [start,path]

	# Will return path to main function
	return Traversal(node,end,visited,dimension,maze)
	
def Traversal(node, end, visited, dimension, maze):
	"""
	Traversal is a recursive function to be used in conjunction with
	DFS. Recursion is necessary to explore the deepest parts of the 
	tree first.

	It will return a call to itself until the path is found. This path
	will be returned to DFS.
	"""

	# Node is of the format [(x,y), [*path to node*]]
	path = node[1]
	coord = node[0]

	# Updates the path.
	path = path + [coord]

	# If the coordinate you're on is the goal node, then return the path.
	if coord == end:
		return path

	# To avoid exploring the same cell in the maze, add it to the visited list.
	visited.append(coord)

	# Explore neighbours
	for neighbour in getNeighbours(coord,dimension):
		# If the neighbour is a passageway and hasn't been evaluated before, go deeper.
		if maze[neighbour[0]][neighbour[1]][1] == False and neighbour not in visited:
			# Calls itself to go deeper into the tree.
			return Traversal([neighbour,path],end,visited,dimension,maze)