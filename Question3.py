
a = 'rats'
b = 'star'


#Function defines whether 2 words are or are not an anagram (1st way)
def isAnagram1(a,b):
	v = []
	for i in a.lower():
		for j in b.lower():  
			if i == j:
				v.append("true")
	if len(v) == len(a) == len(b):
			print("true")
	else:
			print("false")
isAnagram1(a,b)
#Function defines whether 2 words are or are not an anagram (2nd way)
def isAnagram2(a,b):
	a = list(a.lower())
	b = list(b.lower())
	return sorted(a) == sorted(b)
print isAnagram2(a, b)




