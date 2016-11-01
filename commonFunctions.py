def calculateH(node, goal):
	# Heuristic cost is based on (Manhattan) distance from exit.
	H = abs(node[0]-goal[0]) + abs(node[1]-goal[1])
	return H

def getNeighbours(currentNode, dimension):
	# Gets neighbours in the cardinal directions of the given node.
	x = currentNode[0]
	y = currentNode[1]

	neighbours = []
	# Ensures that coordinates outside of the maze can not be counted as neighbours since they do not exist.
	if x>0:
		neighbours.append((x-1,y))
	if x<dimension-1:
		neighbours.append((x+1,y))
	if y>0:
		neighbours.append((x,y-1))
	if y<dimension-1:
		neighbours.append((x,y+1))
	return neighbours

def getJumpNeighbours(currentNode, goal, dimension, maze):
	x = currentNode[0]
	y = currentNode[1]

	neighbours = []

	i = x+1
	while i < dimension:
		if maze[i][y][1] == False:
			if (i,y) == goal:
				return [[(i,y), 0]]

			if y+1 < dimension:
				if maze[i][y+1][1] == False:
					neighbours.append([(i,y), i-x])
			elif y-1 >= 0:
				if maze[i][y-1][1] == False:
					neighbours.append([(i,y), i-x])

		else:
			i = dimension+1
		i += 1

	i = x-1
	while i >= 0:
		if maze[i][y][1] == False:
			if (i,y) == goal:
				return [[(i,y), 0]]

			if y+1 < dimension:
				if maze[i][y+1][1] == False:
					neighbours.append([(i,y), x-i])
			elif y-1 >= 0:
				if maze[i][y-1][1] == False:
					neighbours.append([(i,y), x-i])
		else:
			i = -1
		i -= 1

	j = y+1
	while j < dimension:
		if maze[x][j][1] == False:
			if (x,j) == goal:
				return [[(x,j), 0]]

			if x+1 < dimension:
				if maze[x+1][j][1] == False:
					neighbours.append([(x,j), j-y])
			elif x-1 >= 0:
				if maze[x-1][j][1] == False:
					neighbours.append([(x,j), j-y])
		else:
			j = dimension+1
		j +=1

	j = y-1
	while j >= 0:
		if maze[x][j][1] == False:
			if (x,j) == goal:
				return [[(x,j), 0]]

			if x+1 < dimension:
				if maze[x+1][j][1] == False:
					neighbours.append([(x,j), y-j])
			elif x-1 >= 0:
				if maze[x-1][j][1] == False:
					neighbours.append([(x,j), y-j])
		else:
			j = -1
		j -= 1

	return neighbours



