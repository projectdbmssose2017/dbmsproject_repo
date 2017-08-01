#eike sommer thomas sieron 
#databases sose 2017 tutorium nina kubiessa mi 14-16
#zettel 4 aufgabe 4 python
#quellen: stackoverflow, wiki.postgresql.org

import psycopg2

def einfuegen(elist, tag_string, date_string):
		#print(elist)
		counter=0
		position_el=-1
		hilflist=[]
		while counter < len(elist):				#durchskippen bis datum erreicht und in pos_el markiert
			hilfslist=elist[counter]
			if hilfslist[0]==date_string:
				position_el=counter
				counter=len(elist)
			counter=counter+1
		if position_el==-1:
			print("ERROR!! ")
			print(date_string)
			return elist
		tweet_struct=elist[position_el]				#elist: liste aus listen, datum und folgend liste mit tags und häufigkeit
		tweetlist=tweet_struct[1]				#tweet_struct: datum und tweetlist
		if tweetlist == [" ",0]:				#tweetlist tags und int ihrer haeufigkeit
			tweetlist=[[tag_string, 1],[" ",0]]
			tweet_struct[1]=tweetlist
			elist[position_el]=tweet_struct
			return elist
		else:
			counter=0			
			while counter < len(tweetlist):
				hilfsliste=tweetlist[counter]
				hilfstag=hilfsliste[0]
				if hilfstag==tag_string:
					hilfsl=tweetlist[counter]
					hilfsl[1]=hilfsl[1]+1
					tweetlist[counter]=hilfsl
					tweet_struct[1]=tweetlist
					elist[position_el]=tweet_struct
					return elist
				if hilfstag==" ":
					tweetlist[counter]=[tag_string, 1]					
					tweetlist.append([" ",0])
					tweet_struct[1]=tweetlist
					elist[position_el]=tweet_struct
					return elist
				counter=counter+1


try:
    conn = psycopg2.connect("dbname='election' user='postgres' host='localhost' password='postgres'")
except:
    print ("I am unable to connect to the database")

cur = conn.cursor()
cur.execute("""SELECT * from enthaelt""")
rows = cur.fetchall()
list1=rows
cur.execute("""SELECT * from tweet""")
rows2 = cur.fetchall()
list2=[]
path1='/home/thomas/tweet.txt'
counter=0
hilfsrow=[]
while counter < len(rows2):
	hilfsrow=rows2[counter]
	h1=hilfsrow[0]
	h2_str=hilfsrow[8]
	h2=h2_str[:5]
	hr=[]
	hr.append(h1)
	hr.append(h2)
	list2.append(hr)
	counter=counter+1
#print(len(list1))
#print(len(list2))
#print(list1[0])
#print(list2[0])						#list2 tweetid und datumsangabe
#print(list2[6125])
#print(list1[0])						#list1 tweetid und hashtag
#print(list1[1])
#print(list1[1778])
eliste=[]
tweetlist=[" ",0]
month=1
while month < 10:					#eliste mit datumsangaben fuellen
	day=1	
	while day < 32:
		elem_ergeb=[]
		if day < 10:		
			date="0"+str(day)+".0"+str(month)
		else:
			date=str(day)+".0"+str(month)
		elem_ergeb.append(date)
		elem_ergeb.append(tweetlist)
		eliste.append(elem_ergeb)
		if month==2 and day==29:
			day=32
		elif (month==4 or month==6 or month==9) and day==30:
			day=32
		day=day+1
	month=month+1

counter=0
while counter < len(list1):					#für alle hashtags: einfuegen 
	counter2=0
	element=list1[counter]
	while counter2 < len(list2):
		element2=list2[counter2]
		if element[0]==element2[0]:			#tweetid uebereinstimmend: eintragen in eliste mit datum und hashtag
			eliste=einfuegen(eliste, element[1], element2[1])
			counter2=len(list2)
		counter2=counter2+1
	counter=counter+1

#print(eliste)
print("[")
counter=0
datestr=" "
dtsr=" "
hl=[]
hc=[]
while counter < len(eliste):
	hl=eliste[counter]
	datestr=hl[0]
	dtsr=datestr[3]+datestr[4]+", "+datestr[0]+datestr[1]
	datestr="[app(2017, " + dtsr
	ct_tags=0
	hl2=hl[1]
	if hl2 != [' ', 0]:
		count=0
		while count < len(hl2):
			hc=hl2[count]
			ct_tags=ct_tags+hc[1]
			count=count+1
	datestr=datestr+"), "+str(ct_tags)+"],"
	print(datestr)	 	
	counter=counter+1



