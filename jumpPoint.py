def JumpPoint(start, end, dimension, maze, openCells, closedCells):
	x = start[0]
	y = start[1]

	#openCells.append((x, y, maze[x][y]))

	i = 0
	j = 0

	print start

	while j < len(maze):
		if maze[x][j] != True and j!=y:
			if j+1 < dimension:
				if maze[x][j+1]!= True:
					openCells.append((x,j,maze[x][j]))
			elif (j-1) >0:
				if maze[x][j-1]!= True:
					openCells.append((x,y,maze[x][j]))
		j +=1


	while i < len(maze):
		if maze[i][y] != True and i!=x:
			if i+1 <dimension:
				if maze[i+1][y]!= True:
					openCells.append((i,y,maze[i][y]))
			elif i-1 <dimension:
				if maze[i-1][y]!= True:
					openCells.append((i,y,maze[i][y]))
		i +=1

	minCostCell = openCells[0]
	for cell in openCells:
		if cell[2] < minCostCell[2]:
			minCostCell=cell

	print minCostCell
	print openCells
	print closedCells

	n = Nodes(3)
	x = Nodes(4)
	d = Nodes(5)

	n.add_childNode(x)
	x.add_childNode(d)

	for node in n.children:
		print node.data

	#if end[0]!=minCostCell[0] and end[1]!=minCostCell[1]:
	#	newStart = (minCostCell[0],minCostCell[1])
	#	JumpPoint(newStart, end, dimension, maze)