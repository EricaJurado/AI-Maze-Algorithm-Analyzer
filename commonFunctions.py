def calculateH(node, goal):
	# Heuristic cost is based on (Manhattan) distance from exit.
	H = abs(node[0]-goal[0]) + abs(node[1]-goal[1])
	return H

def getNeighbours(currentNode, dimension):
	point = currentNode[0]
	x = point[0]
	y = point[1]
	neighbours = []
	if x>0:
		neighbours.append((x-1,y))
	if x<dimension-1:
		neighbours.append((x+1,y))
	if y>0:
		neighbours.append((x,y-1))
	if y<dimension-1:
		neighbours.append((x,y+1))
	return neighbours
