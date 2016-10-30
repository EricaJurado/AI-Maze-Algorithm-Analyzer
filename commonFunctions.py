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
