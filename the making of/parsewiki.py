from gensim.corpora import wikicorpus as wc

def parse(i=1)
	print "processing wikipedia file a",i
	wiki = wc.WikiCorpus("./a" + str(i) + ".bz2")
	wiki.save("./a" + str(i))
	
if __name__ == "__main__":
	parse(int(sys.argv[1]))

