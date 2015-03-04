"""Command line arguments

Usage:

python command_line.py(5, 4) 

Prints 5+4 = 9
"""


def my_add(arg1, arg2):
	return arg1 + arg2

if __name__ == "__main__":
	import sys 
	print sys.argv
	print my_add(int(sys.argv[1]), int(sys.argv[2]))