from commonFunctions import calculateH
from commonFunctions import getJumpNeighbours

def JumpPoint(start, goal, maze):
	dimension = len(maze)
	
	openList = [] #set of nodes to be evaluated
	closedList = [] #set of nodes already evaluated

	# Hcost is the heuristic cost of a node to the goal (Manhattan distance is used).
	Hcost = calculateH(start, goal)
	path = []
	start = [start, 0, Hcost, path]

	#point, g cost (distance from starting node/distance travelled), h cost (distance from end node)
	openList.append(start)

	# While our openList is not empty, we still have nodes to evaluate
	while openList:
		print "openList" + str(openList)
		print "closedList" + str(closedList)
		# Arbitarily set our current node to the first on in the openList.
	 	current = openList[0]
	 	print "current" + str(current)

	 	# This will be used to determine the new Gcost of the path for successive nodes.
	 	currentGCost = current[1]

	 	# Then loop through the list of nodes to find the node with the lowest F cost.
	 	# The f cost is caluculate by added the g and h costs of the node in question.
	 	for node in openList:
	 		if (node[1]+node[2]) < (current[1]+current[2]):
	 			current = node

	 	path  = current[3]
	 	path = path + [current[0]]
	 	print path

	 	# Then remove the node with the lowest cost from the lowest list.
	 	openList.remove(current)
	 	# And add this node to the closed list since we've evaluated it.
	 	inClosed = False
	 	for closed in closedList:
	 		if closed[0] == current[0]:
	 			inClosed = True

	 	if inClosed == False:
	 		closedList.append(current)

	 	# If the current node is the goal, we know that we've found out path.
	 	if current[0] == goal:
	 		return path

	 	# Get the neighbours of our current node.
	 	neighbours = getJumpNeighbours(current[0], goal, dimension,maze)
	 	print "neighbours" + str(neighbours)
	 	print openList
	 	print closedList
	 	# Then loop through the neighbours
	 	for neighbour in neighbours:
	 		Hcost = calculateH(neighbour[0], goal)
	 		addedGCost = neighbour[1]
	 		neighbour = [neighbour[0], currentGCost+addedGCost, Hcost, path]
	 		x = neighbour[0][0]
	 		y = neighbour[0][1]

	 		# Check to see if the neighbour is traversable or if it's in the closedList (meaning we've already evaluated it and do not need to do so again.).
	 		closed = False
	 		length = len(closedList)-1
	 		while length > 0:
	 			if closedList[length][0] == (x,y):
	 				closed=True
	 				length=-1
	 			length -=1

	 		# If the node is traversable and is not in the closedList, we don't need to skip to the next neighbour.
	 		if closed == False:
	 			# Now we want to see if the new path to the neighbour is shorter (meaning it has a smaller G cost) or if the neighbor isn't in the openList.

	 			newPathCost = currentGCost + 1 #gcost of previous node plus cost of travel
	 			oldGCost = -1

	 			# See if newpath is shorter than existing path by looking at the old Gcost.
	 			for node in openList:
	 				if node[0]==(x,y):
	 				 	oldGCost = node[1]

	 			# Check and see if node is in the openList
	 			inOpen = False
	 			for openNode in openList:
	 				# if openNode[0] == current[0]:
	 				inOpen = True

	 			# If the new path to the node is less than the old cost or if it's in open
	 			if newPathCost < oldGCost or inOpen:
	 				# Remove it from the openList and set newNode
	 				openList.remove(node)
	 				closedList.append(node)
	 				newNode = [node[0], newPathCost, node[2]]
	 				#newNode.parent = currentNode

	 			if inOpen == False:
	 				openList.append(neighbour)