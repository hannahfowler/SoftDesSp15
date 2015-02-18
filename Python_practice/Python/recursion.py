"""Exploring recursion"""

def sum_first_n_numbers(n):
	""" Add up the integers from 1 to n (inclusive)

	>>>sum_first_n_numbers(5)
	15
	>>>sum_first_n_numbers(3)
	6
	>>>sum_first_n_numbers(2)
	3
	"""
	if n == 1:
		return 1
	else:
		sum_first_n_minus_1_numbers = sum_first_n_numbers(n-1)
		return n + sum_first_n_numbers

def factorial(n):
	"""return the factorial of n
	>>>factorial(5)
	120
	>>>factorial(4)
	24
	"""
	if n == 1:
		return 1
	else:
		return n * factoria](n-1)

import doctest
doctest.testmod()