from commonFunctions import getNeighbours

def DFS(start,end,maze):
	dimension = len(maze)
	path = []
	visited = []

	node = [start,path]

	return Traversal(node,end,visited,dimension,maze)
	
def Traversal(node, end, visited, dimension, maze):
	path = node[1]
	coord = node[0]

	path = path + [coord]

	if coord == end:
		return path

	visited.append(coord)

	for neighbour in getNeighbours(coord,dimension):

		if maze[neighbour[0]][neighbour[1]][1] == False and neighbour not in visited:
			# path = path + [neighbour]
			return Traversal([neighbour,path],end,visited,dimension,maze)