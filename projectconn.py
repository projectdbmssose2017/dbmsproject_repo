#eike sommer thomas sieron 
#databases sose 2017 tutorium nina kubiessa mi 14-16
#project iteration2 aufgabe 4 / python
#quellen: stackoverflow, wiki.postgresql.org


import csv
import psycopg2

with open('american-election-tweets.csv') as csvfile:
		csv_data = csv.reader(csvfile)

try:
    conn = psycopg2.connect("dbname='election' user='postgres' host='localhost' password='dbmsproject'")
except:
    print ("I am unable to connect to the database")



cur = conn.cursor()
cur.execute("""INSERT INTO account (handle, benutzername) 
		VALUES ('HillaryClinton', 'Hillary Clinton');""")
cur.execute("""INSERT INTO account (handle, benutzername)
		VALUES ('realDonaldTrump', 'Donald Trump');""")

'''
for row in csv_data:
	cur.execute("INSERT INTO hashtag (tag)" "VALUES (%s)", row)
'''

cur.close()
conn.commit()
conn.close()

print("CSV data imported")



