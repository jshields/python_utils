#!/bin/python
# jshields
import logging
from animal import Animal


class Dog(Animal):
	def __init__(self, name, breed, color):
		self.species = u'canine'
		self.name = name
		self.breed = breed
		self.color = color
		_emoji = ur'\u1F436' # dog-face

		# arbitrarily (?) validating name as being valid unicode
		# TODO decide whether or not to keep this... Maybe the classes should be Jinja compatible
		#try:
		#	self.name = unicode(name, 'utf_8', strict)
		#except ValueError:
		#	logging.critical('Non-Unicode String passed as name')
		#self.breed = unicode(breed, 'utf_8', replace)
		#self.color = unicode(color, 'utf_8', replace)
		logging.info("%s initialized" % self)

	def __str__(self):
		return u'<Dog name=%s species=%s breed=%s color=%s emoji=%s >' % (self.name, self.species, self.breed, self.color, Dog.emoji())




"""
#convert to unicode
teststring = unicode(teststring, 'utf-8')
#encode it with string escape
teststring = teststring.encode('unicode_escape')
"""