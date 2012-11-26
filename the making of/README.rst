Data source
-----------

http://dumps.wikimedia.org/enwiki/latest/

Included files
--------------

	enwiki-latest-pages-articles1.xml-p000000010p000010000.bz2
		2012-Nov-02 06:14:33	40.4M	application/x-bzip
	enwiki-latest-pages-articles2.xml-p000010002p000024999.bz2
		2012-Nov-02 06:15:27	66.0M	application/x-bzip
	enwiki-latest-pages-articles3.xml-p000025001p000055000.bz2
		2012-Nov-02 06:16:58	100.4M	application/x-bzip
	enwiki-latest-pages-articles4.xml-p000055002p000104998.bz2
		2012-Nov-02 06:17:37	101.7M	application/x-bzip
	enwiki-latest-pages-articles5.xml-p000105002p000184999.bz2
		2012-Nov-02 06:21:21	136.5M	application/x-bzip
	enwiki-latest-pages-articles6.xml-p000185003p000305000.bz2
		2012-Nov-02 06:21:05	163.7M	application/x-bzip
	enwiki-latest-pages-articles7.xml-p000305002p000464996.bz2
		2012-Nov-02 06:23:11	188.7M	application/x-bzip
	enwiki-latest-pages-articles8.xml-p000465001p000665000.bz2
		2012-Nov-02 06:25:02	179.6M	application/x-bzip
	enwiki-latest-pages-articles9.xml-p000665001p000925000.bz2
		2012-Nov-02 06:27:04	176.1M	application/x-bzip
	enwiki-latest-pages-articles10.xml-p000925001p001325000.bz2
		2012-Nov-02 06:31:30	252.4M	application/x-bzip
	enwiki-latest-pages-articles11.xml-p001325001p001825000.bz2
		2012-Nov-02 06:32:20	262.5M	application/x-bzip
	enwiki-latest-pages-articles12.xml-p001825001p002425000.bz2
		2012-Nov-02 06:35:38	286.2M	application/x-bzip
	enwiki-latest-pages-articles13.xml-p002425002p003124997.bz2
		2012-Nov-02 06:37:45	270.5M	application/x-bzip
	enwiki-latest-pages-articles14.xml-p003125001p003924999.bz2
		2012-Nov-02 06:36:39	270.9M	application/x-bzip
	enwiki-latest-pages-articles15.xml-p003925001p004824998.bz2
		2012-Nov-02 06:39:35	261.5M	application/x-bzip
	enwiki-latest-pages-articles16.xml-p004825005p006024996.bz2
		2012-Nov-02 06:43:34	320.6M	application/x-bzip
	enwiki-latest-pages-articles17.xml-p006025001p007524997.bz2
		2012-Nov-02 06:46:14	328.5M	application/x-bzip
	enwiki-latest-pages-articles18.xml-p007525004p009225000.bz2
		2012-Nov-02 06:46:56	348.6M	application/x-bzip
	enwiki-latest-pages-articles19.xml-p009225002p011124997.bz2
		2012-Nov-02 06:45:55	327.9M	application/x-bzip
	enwiki-latest-pages-articles20.xml-p011125004p013324998.bz2
		2012-Nov-02 06:56:06	438.6M	application/x-bzip
	enwiki-latest-pages-articles21.xml-p013325003p015724999.bz2
		2012-Nov-02 06:57:01	459.1M	application/x-bzip
	enwiki-latest-pages-articles22.xml-p015725013p018225000.bz2
		2012-Nov-02 06:56:06	416.6M	application/x-bzip
	enwiki-latest-pages-articles23.xml-p018225004p020925000.bz2
		2012-Nov-02 06:59:46	489.5M	application/x-bzip
	enwiki-latest-pages-articles24.xml-p020925002p023724999.bz2
		2012-Nov-02 07:07:38	542.7M	application/x-bzip
	enwiki-latest-pages-articles25.xml-p023725001p026625000.bz2
		2012-Nov-02 07:01:45	573.2M	application/x-bzip
	enwiki-latest-pages-articles26.xml-p026625004p029624976.bz2
		2012-Nov-02 07:00:55	535.2M	application/x-bzip
	enwiki-latest-pages-articles27.xml-p029625017p037517228.bz2
		2012-Nov-02 08:15:33	1.4G	application/x-bzip

Python code
------------
You'll need the gensim package.

1. parsewiki.py <num> reads "./a<num>bz2" wikipedia file and stores result
   in "./a<num>"
2. countwords.py <num> reads "./a<num>" file, filters words and stores
   word occurances in "./db<num>" file (a pickled defaultdict(int))
3. mergedb.py <from> <to> reads files "./db<from>" till "./db<to>", adds
   word occurances and stores result in "./db" (pickled) and "./dbfile.py"
   (python code - much faster)

