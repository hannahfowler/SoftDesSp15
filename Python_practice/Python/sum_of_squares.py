def sum_of_squares(n):
	squares = []
	for i in range(n+1):
		x = i**2
		squares.append(x)

	total = sum(squares)
	return total
	

print sum_of_squares(4)
