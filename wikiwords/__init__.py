from . import occdb
from . import freqdb

def freq(word, notfound=None):
	"""Return frequency of given word.
	If not found, return notfound(word) or 0.0"""
	if word in freqdb.db:
		return freqdb.db[word]
	elif notfound:
		return notfound(word)
	else:
		return 0.0

def occ(word):
	"""Return number of occurances of given word.
	If not found, return notfound(word) or 0"""
	if word in occdb.db:
		return occdb.db[word]
	elif notfound:
		return notfound(word)
	else:
		return 0

W = 105940.
N = 2194549780.
