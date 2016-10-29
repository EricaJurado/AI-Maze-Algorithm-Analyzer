def Prim(size):
	"""

	Prim's algorithm works by carving out pathways into the maze. Prim's algorithm generates a
	spanning tree where the nodes of the graph and the spanning tree are the cells of the maze.
	A frontier is an edge where the algorithm can move from one cell to an adjacent cell.

	"""

	# Initializes walls.
	i = size
	j = size
	#walls = [(i,j) for i in range(size) for j in range(size)]
	grid = [[[(i,j),True] for i in range(size)] for j in range(size)] #True=wall False=pass

	# Picks an initial cell at some point in the maze.
	x = random.randint(0, size-1)
	y = random.randint(0, size-1)
	frontiers = [(x,y,x,y)]
	startNode = (x,y)
	endNode = (x,y)

	while (len(frontiers) > 0):
		index = random.randint(0, len(frontiers)-1)
		f = frontiers[index]
		x = f[2]
		y = f[3]

		if (grid[x][y][1] == True):
			grid[f[0]][f[1]][1] = False
			grid[x][y][1] = False
			if ( x >= 2 and grid[x-2][y][1] == True):
				frontiers.append((x-1, y, x-2, y))
			if ( y >= 2 and grid[x][y-2][1] == True):
				frontiers.append((x, y-1, x, y-2))
			if ( x < size-2 and grid[x+2][y][1] == True):
				frontiers.append((x+1, y, x+2, y))
			if ( y < size-2 and grid[x][y+2][1] == True):
				frontiers.append((x, y+1, x, y+2))

		endNode = (x,y)
		del frontiers[index]

	return (startNode, endNode, grid)