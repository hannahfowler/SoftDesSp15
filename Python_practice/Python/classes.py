"""Working with Python classes """ 
#Social networking around work 

import copy 
def my_function():
	"""Some function """
	pass

class Person(object):
	"""Representation of a person"""
	def __init__(self, first_name, last_name, job, height):
		""" Initializing a person object given some info"""
		print "I am in the init method"
		self.first_name = first_name
		self.last_name = last_name
		self.job = job
		self.height = height

	def print_person(self):
		"""Prints out person's atributes"""
		template = "{first} {last} is a {job}"
		print template.format(first = self.first_name, last = self.last_name, job = self.job, height = self.height)

#Create a new hfowler Person and assign attributes
hfowler = Person("Hannah", "Fowler", "student", [5,3]) 
hfowler.first_name = 'Hannah'
hfowler.last_name = 'Fowler'
hfowler.job = 'student'
hfowler.height = [5, 3]

hfowler.print_person()

