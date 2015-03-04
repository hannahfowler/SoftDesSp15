"""fp = open('name_of_text.txt')
print fp.read()
fp.seek()
fp.close()
fp.open("alice.txt")
"""

"""Process text files into Pig Latin

Usage:

Prints out the text converted to Pig Latin 
"""

def process_text(filename):
	"""Print filename translated into Pig latin"""
	fp = open(filename, 'r')
	for line in fp:
		for word in line.split():
			print word 
			#Process into pig latin


if __name__ == "__main__":
	import sys
	filename = sys.argv
	print "filename given was" , filename
	process_text(filename)

