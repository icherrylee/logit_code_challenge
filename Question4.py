
a = [1,2,3,6]

#Funtion returns the mean of an array'a'
def mean(a):
	x = 0
	for i in a:
		x += i

	return x/len(a)

print mean(a)

#Function returns the standard deviation of an array 'a'
def stdv(a):
	counter = 0
	for i in a:
		y = (i - mean(a))**(2)
		counter = y + counter
	return (counter / float(len(a)))**(.5)

print stdv(a)