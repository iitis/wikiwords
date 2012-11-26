Frequency of words in the English 2012 Wikipedia
================================================

This Python module can be used to quickly retrieve absolute word frequency
for English language, as used in Wikipedia articles as of year 2012.

Author: Paweł Foremski <pjf@iitis.pl>, IITiS PAN www.iitis.pl

Usage
-----
	>>> import wikiwords
	>>> wikiwords.freq("monty")
	6.348454761413523e-06
	>>> wikiwords.occ("python")
	18972
	>>> wikiwords.freq("no such word", lambda x: 1./len(x))
	0.08333333333333333

Installation
------------
	$ sudo pip install wikiwords

Details
-------


Wikipedia files were downloaded on 23.11.2012

The corpus was filtered:

1. all words containing non-latin letters were removed (A-Z)
2. in single files (see below), words with frequency < 5e-7 were removed
3. in the final file (28 files merged), words with f < 5e-8 were removed
4. all words shorter than 2 characters were removed (see below)

The final corpus contains over 100,000 words with over 2 billion occurances.

For copyright information on data, see
	http://en.wikipedia.org/wiki/Wikipedia:Copyrights

The Python source code is licensed to you under the GNU GPL v3

See "the making of/" subdirectory for details on how the data was created.

The single letter words
-----------------------
The single-letter words were removed by the gensim parser. In order to address
this, relevant frequencies and number of occurances were artifically injected
from the Google Web Trillion Word Corpus, described by Thorsten Brants and Alex
Franz in 2006 [1]. For more information -- and for an example of possible
application of wikiwords.py -- see Peter Norvig ngrams site at [2].

1. http://googleresearch.blogspot.com/2006/08/all-our-n-gram-are-belong-to-you.html
2. http://norvig.com/ngrams/

