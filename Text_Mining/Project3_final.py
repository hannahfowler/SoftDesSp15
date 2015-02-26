"""Final Documentation for Project 3 Word Cloud"""

import operator 
from PIL import Image 
from PIL import ImageDraw as ImageDraw
from PIL import ImageFont as ImageFont
import random as random 

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", '*', '-']

with open('Wuthering_Heights.txt') as f:
	lines = f.readlines()
text = "".join(lines)

def remove_punct(text_name):
	for line in text_name:
		for word in line:
			if (word in punctuation and word in text):
				text_name = text_name.replace(word, "")
	return text_name  

def frequency(text_name):
	""" From given text file produces a list of tuples of words and 
	    their frequency
	    Returns the top 100 words 
		input: text 
		output: list 
	"""
	my_dict = {}
	for word in text_name.split():
		my_dict[word] = my_dict.get(word, 0) + 1  
	sorted_my_dict = sorted(my_dict.items(), key=operator.itemgetter(1))
	while len(sorted_my_dict) != 100:
		sorted_my_dict.remove(sorted_my_dict[0])
		return sorted_my_dict

def generate_art(filename, text_name, x_size=350, y_size=350):
	"""Generates the image of word cloud and saves as an image filename
		filename: string filename for image (save as png)
		dictionary: give words to include in word cloud 
		x_size, y_size: optional for setting size of image 
	"""
	texts = []
	occurences = []
	words = frequency(text_name)
	im = Image.new("L", (512,512), "black")
	d = ImageDraw.Draw(im)
	for element in words:
		for thing in element:
			if type(thing) == str:
				texts.append(thing)
			if type(thing) == int:
				occurences.append(thing)
	for i in range(len(texts)):
		f = ImageFont.truetype("AmaticSC-Regular.ttf", 10 * occurences[i])
		sizes = f.getsize(texts[i])
		d.text((0+sizes[0], 0+sizes[1]), texts[i], font = f, fill = 255) 
	im.save(filename)
no_punct = remove_punct(text)
generate_art('testrun2.png', no_punct)