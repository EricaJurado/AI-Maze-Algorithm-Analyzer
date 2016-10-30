import random

def Prim(size):
	"""

	Prim's algorithm works by carving out pathways into the maze. Prim's algorithm generates a
	spanning tree where the nodes of the graph and the spanning tree are the cells of the maze.
	A frontier is an edge where the algorithm can move from one cell to an adjacent cell.

	Prim's algorithm is a greedy algorithm meaning that it finds a minimum spanning tree. For 
	our maze generation, the cost of travelling from one node to another has uniform cost. Note
	that it is only possible to move in the 4 cardinal directions and NOT diagonally. 

	"""

	i = size
	j = size
	# Initializes walls. Note that initally all cells are walls
	grid = [[[(j,i),True] for i in range(size)] for j in range(size)] #True=wall or nontraversable, False=passage or traversable

	# Picks an starting point at some cell in the maze.
	x = random.randint(0, size-1)
	y = random.randint(0, size-1)
	frontiers = [(x,y,x,y)]
	
	passages = []

	while (len(frontiers) > 0):
		# Chooses a random index in our list of frontiers.
		index = random.randint(0, len(frontiers)-1)

		# Gets the element in the random index we've selected.
		f = frontiers[index]
		del frontiers[index]
		x = f[2]
		y = f[3]

		# Checks if the element we've selected in a wall or not.
		if (grid[x][y][1] == True):
			# Turn that wall into a passageway
			grid[x][y][1] = False
			grid[f[0]][f[1]][1] = False
			passages.append((x,y))
			#passages.append((f[1],f[x]))

			# Now that we've updated the passageways, we'll need to add the frontiers of this new pasageway to our list.
			if ( x >= 2 and grid[x-2][y][1] == True):
				frontiers.append((x-1, y, x-2, y))
			if ( y >= 2 and grid[x][y-2][1] == True):
				frontiers.append((x, y-1, x, y-2))
			if ( x < size-2 and grid[x+2][y][1] == True):
				frontiers.append((x+1, y, x+2, y))
			if ( y < size-2 and grid[x][y+2][1] == True):
				frontiers.append((x, y+1, x, y+2))

		# Since the node is no longer a fronter, we need to delete it from the list.

	startNode = passages[0]
	endNode = passages[-1]
	# Returns our starting node, our ending node, and the maze itself.
	return (startNode, endNode, grid)