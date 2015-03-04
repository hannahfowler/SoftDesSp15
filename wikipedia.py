"""Getting dat source from Wiki"""

from pattern.web import *
w = Wikipedia()
article = w.search('Hannah')
for section in article.sections:
	print repr(' ' * section.level + section.title)
