"""Mini Project 3"""
from pattern.en import *
import string 

wuthering_heights_full_text = open('Wuthering_Heights.txt', 'r')
stop_words_list = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'", '*', '-']

def text_to_list(textname): 
	"""Transforms given text to a list of words. """ 
	word_list = []
	for line in textname:
		for word in line.split():
			word_list.append(word)
	return word_list

def remove_punct(textname):
	word_list = text_to_list(textname)
	"""Removes the punctuation from given text file"""
	for element in word_list:
		if (ch in element and ch in punctuation):
			word_list.remove(element)
	return word_list
print remove_punct(wuthering_heights_full_text)
def remove_stopwords(given_list):
	"""Removes stopwords(common English words such as 'to', 'a', 'and') from given text file with no punctuation"""
	important_words = []
	for element in stop_words_list:
		if element not in given_list:
			important_words.append(element)
	return important_words

def frequency(list_given):
	my_dict = {}
	for element in list_given:
		my_dict[element] = my_dict.get(element, 0) + 1
	return my_dict

def list_to_sentence(list_given):
	sentence = ' '.join(list_given)
	return sentence

def top_100(textname1, textname2):
	important_words = remove_stopwords(textname1, textname2)
	just_words = remove_punct(important_words)
	frequencies = frequency(just_words)
	my_dictList = zip(frequencies.values(), frequencies.keys())
	my_dictList.sort()
	while len(my_dictList) != 50:
		"""for tuples in my_dictList:
			if tuples[0] > 100:
				my_dictList.remove(tuples)"""
		my_dictList.remove(my_dictList[0])
	return my_dictList

def final(textname):
	word_list = text_to_list(wuthering_heights_full_text)
	no_punct = remove_punct(word_list)

final(wuthering_heights_full_text)


