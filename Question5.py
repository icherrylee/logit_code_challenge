def cumulative(observations):
	totalEvents = []
	totalSum = 0
	for i in observations:
		totalSum = totalSum + i
		totalEvents.append(totalSum)
	return totalEvents

print cumulative([2, 3, 1])
print cumulative([10, 20, 30])







