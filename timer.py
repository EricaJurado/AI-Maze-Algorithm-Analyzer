from timeit import default_timer as timer

def algorithm_timer(algorithm, start, end, maze):
	timerStart = timer()
	algorithm(start,end,maze)
	timerEnd = timer()
	totalTime = timerEnd-timerStart
	return totalTime


