from commonFunctions import getNeighbours
import heapq


def UniformCostDijkstra(start, goal, maze):
	dimension = len(maze)
	cost = 0

	# Used to hold nodes, the node popped off will be the one with the lowest cost.
	frontier = [(0,start,[])]

	# Will hold nodes that have been evaluated.
	explored = {}

	# While the frontier is not empty continue with search. 
	while frontier:
		# Gets information on lowest cost node in frontier. 
		cost, node, path = heapq.heappop(frontier)

		# If node has been explored and it has a lower cost then bail out of current iteration of loop.
		if explored.has_key(node) and explored[node] < cost:
			continue

		# Update the path with the new node.
		path = path + [node]

		# If the node we're on is the goal, then the path is now finished.
		if node == goal:
			return path

		# Get the neighbours and iterate through them.
		for neighbour in getNeighbours(node,dimension):
			# Calculate basic cost
			neighbourcost = 1
			if neighbour == goal:
				neighbourcost = 0

			# If the neighbour has not been explored, add to heap.
			if neighbour not in explored:
				heapq.heappush(frontier, (cost+neighbourcost, neighbour, path))

		# Add the node to the explored items. 
		explored[node] = cost
	return None