import sys
import cPickle as pickle
from collections import defaultdict

def add_dict(db1, db2):
	for k,v in db2.items():
		db1[k] += v
	return db1

def merge(a=1, z=27):
	dbs = []
	
	for i in xrange(a, z+1):
		print "loading db" + str(i)
		f = open("./db" + str(i))
		dbs.append(pickle.load(f))
		f.close()

	db = reduce(add_dict, dbs)

	# filter really rare words (<0.000005%)
	T = int(5e-8 *  sum(db.itervalues()))
	for k,c in db.items():
		if c < T:
			del db[k]

	f = open("./db", "w")
	pickle.dump(db, f)
	f.close()
	
	f = open("./dbfile.py", "w")
	f.write(str(db))
	f.close()

	print "done"
	print "(edit dbfile.py before using)"

if __name__ == "__main__":
	merge(int(sys.argv[1]), int(sys.argv[2]))

