#eike sommer thomas sieron 
#databases sose 2017 tutorium nina kubiessa mi 14-16
#project iteration2 aufgabe 4 / python
#quellen: stackoverflow, wiki.postgresql.org, laurivan.com


import csv
import psycopg2




try:
    connect = psycopg2.connect("dbname='election' user='postgres' host='localhost' password='dbmsproject'")
except:
    print ("I am unable to connect to the database")



cur = connect.cursor()


#cur.execute("""INSERT INTO account (handle, benutzername)
#		VALUES ('HillaryClinton', 'Hillary Clinton');""")			#fuellen table account
#cur.execute("""INSERT INTO account (handle, benutzername)
#		VALUES ('realDonaldTrump', 'Donald Trump');""")

cur.execute("""CREATE TABLE alles (tweetid int, handle varchar(16), text varchar(140), is_retweet varchar(16), original_author varchar (140), time varchar(20), in_reply_to_screenname varchar(140), is_quote_status varchar(16), retweet_count varchar(16), favorite_count varchar(16), source_url varchar(2000), truncated varchar(16));""") 			#anlegen einer hilfstabelle alles zum dateiauslesen
						#beachte 12 spalten, alles strings

connect.commit()



with open('/home/thomas/american-election-tweets-test.csv') as file:
	reader = csv.reader(file, delimiter = ";")
	counter=0
	for row in reader:
		cur.execute("""INSERT INTO alles (tweetid, handle, text, is_retweet, original_author, time, in_reply_to_screenname, is_quote_status, 			retweet_count, favorite_count, source_url, truncated) VALUES (99999,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""", row)
		cur.execute("""UPDATE alles SET tweetid = %s WHERE tweetid = 99999;""", (counter,))
		counter=counter+1 
		

connect.commit()


cur.execute("""INSERT INTO erwaehnt_account (tweetid, handle) SELECT tweetid, original_author FROM alles WHERE is_quote_status='True';""")

cur.execute("""INSERT INTO twittert (tweetid, handle) SELECT tweetid, handle FROM alles WHERE tweetid > 0;""")

cur.execute("""INSERT INTO tweet (tweetid, text, anzahlfavoriten, anzahlretweets, sourceurl, isretweet, originalautor ) SELECT tweetid, text, 99999, 99999, source_url, 'FALSE', original_author FROM alles WHERE tweetid >0;""")

cur.execute("""INSERT INTO enthaelt (tweetid) SELECT tweetid FROM alles WHERE is_quote_status='True';""")

	

"""
to_timestamp(time FROM alles,'YYYY-MM-DDThh24:mm:ss')::timestamp without time zone, CAST(favorite_count AS INT), CAST(retweet_count AS INT), source_url, CAST(is_retweet AS BOOLEAN), 

platzhalter für alle 4 sachen noch aufloesen

--
hashtags aus den tweets rausparsen und zuordnen???
"""					
#cur.execute(INSERT INTO hashtag (tag) ;)
#cur.execute("""INSERT INTO gemeinsam_getwittert_mit (tag1, tag2, tweetid) SELECT tweetid;""")



connect.commit()

cur.execute("""DROP TABLE alles;""")

connect.commit()
cur.close()
connect.close()
print("CSV data imported")



