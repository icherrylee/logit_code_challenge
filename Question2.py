
#Defines function that creates all combination sets of 2 arrays
def combo(a,b):
	c = []

	for i in a:
		for k in b:
			c.append([i,k])
	print c
	
#input arrays
a = [1, 2, 3]
b = [4, 5, 6]

#calls function 
combo(a, b)
