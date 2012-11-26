import sys
import pickle
from collections import defaultdict
from gensim.corpora import wikicorpus as wc

def readfile(num=1):
	db = defaultdict(int)
	
	f = open("./a" + str(num))
	a = pickle.load(f)
	f.close()
	
	counter = 0
	for text in a.get_texts():
		for word in text:
			if str.isalpha(word):
				counter += 1
				db[word] += 1

	# filter infrequent words (<0.00005%)
	T = int(5e-7 * counter)
	for k,c in db.items():
		if c < T:
			del db[k]

	f = open("./db" + str(num), "w")
	pickle.dump(db, f)
	f.close()

if __name__ == "__main__":
	readfile(int(sys.argv[1]))
