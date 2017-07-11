#eike sommer thomas sieron 
#databases sose 2017 tutorium nina kubiessa mi 14-16
#zettel 4 aufgabe 4 python
#quellen: stackoverflow, wiki.postgresql.org

import psycopg2


try:
    conn = psycopg2.connect("dbname='election' user='postgres' host='localhost' password='postgres'")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("""SELECT * from gemeinsam_getwittert_mit""")
rows2 = cur.fetchall()
#print ("hashtags:")
#print(rows)
#print(len(rows))
#print(rows[len(rows)-1])
#print(rows[0])
cur.execute("""SELECT * from hashtag""")
rows = cur.fetchall()
#print(rows2[len(rows2)-1])
#print(rows2[0])
path1='/home/thomas/tags.txt'
path2='/home/thomas/tagpaare.txt'
tags_file=open(path1,'w')
counter=0
while counter < len(rows):
	hilfsrow=rows[counter]
	tags_file.write("'")
	tags_file.write(hilfsrow[0])
	tags_file.write("',")
	counter =counter+1
tags_file.close()
tagpaare_file=open(path2,'w')
counter=0
while counter < len(rows2):
	hilfsrow=rows2[counter]
	tagpaare_file.write("'")
	tagpaare_file.write(hilfsrow[0])
	tagpaare_file.write("','")
	tagpaare_file.write(hilfsrow[1])
	tagpaare_file.write("',")
	counter =counter+1
tagpaare_file.close()

