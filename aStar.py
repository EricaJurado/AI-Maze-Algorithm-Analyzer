from dataStructures import Tree

t = Tree("jump")
t.root.addChild("a")
t.root.addChild("b")
t.root.getChild("a").addChild("c")
print t.root.getChild("a").parent


def aStar(start, goal, maze):
	dimension = len(maze)
	openList = []
	closedList = []

	#point, g cost, h cost
	Hcost = calculateH(start, goal)
	openList.append([start,0,Hcost])

	while openList:
	 	current = openList[0]
	 	for node in openList:
	 		if (node[1]+node[2]) < (current[1]+current[2]):
	 			current = node

	 	openList.remove(current)
	 	closedList.append(current)

	 	if current[0] == goal:
	 		#path has been found
	 		return

	 	neighbours = getNeighbours(current, dimension)
	 	print neighbours
	 	for neighbour in neighbours:
	 		x = neighbour[0]
	 		y = neighbour[1]

	 		#check if it's traversable
	 		closed = False
	 		length = len(closedList)-1
	 		while length > 0:
	 			if closedList[length][0] == (x,y):
	 				closed=True
	 				length=-1
	 			length -=1

	 		if closed == False and maze[x][y][1]==False:
	 			inOpen = False
	 			for openNode in openList:
	 				if openNode[0] == (x,y):
	 					inOpen = True
	 					print "neighbor is in open!"

	 			Gcost=maze[x][y]



	 		#if maze[x][y][1] == True:

	 	break

