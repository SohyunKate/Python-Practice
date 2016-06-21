#Practice 06-1 구구단 2단! 


def GuGu(n):
	result = []
	i=1
	while i<10:
		result.append(n*i)
		i=i+1
	
	print (result)

result = GuGu(2)
