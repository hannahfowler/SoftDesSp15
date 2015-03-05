""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string 
import itertools 
import operator 
punctuation = string.punctuation

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""

	f = open(file_name, 'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:] 
	list_of_lines = []
	for line in lines:
		out = line.translate(string.maketrans("",""), string.punctuation)
		s = out.strip(string.whitespace) 
		final = s.lower()
	 	list_of_lines.append(final)
	list_of_words = []
	for ele in list_of_lines:
		words = ele.split()
		list_of_words.append(words)
	return list(itertools.chain(*list_of_words))
 

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequentlyoccurring
	"""
	d = dict()
	for word in word_list:
		d[word] = d.get(word, 0)+ 1
	ordered = sorted(d.items(), key=operator.itemgetter(1))
	while len(ordered) != n:
		ordered.remove(ordered[0])
	return ordered   
	
word_list = get_word_list('Heart.txt')
get_top_n_words(word_list, 100)