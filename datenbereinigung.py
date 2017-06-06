#DBS: Projektgruppe 42 IterationII Datenbereinigung via Python 
#https://stackoverflow.com/questions/14471049/python-2-7-1-how-to-open-edit-and-close-a-csv-file
#https://docs.python.org/3.5/library/csv.html

import csv # learn more: https://python.org/pypi/csv Funktion zum Bearbeiten von CSV Dateien
import operator #Funktionsmodul fuer standardoperatoren (e.g., add)
import pandas as pd #import pandas as pd #Funktionsmodul fuer rearrange und addnewcolumn
print('Folgendermaßen sind die Attribute des Datensatzes american-election-tweets.csv (DB "Election") geordnet: (Spaltennummer) Spaltenname \n \n (0) TweetID, (1) handle, (2) text, (3) is_retweeted, (4) original_author, (5) time_date, (6) time_UTCtime, (7) retweet_count, (8) favorite_count, (9) source_url, (10) Len(word), (11) Account_Mention1, (12) Hashtag1, (n) HashtagN / Account_MentionN \n \n Hinweis: Die Spaltenanzahl variiert mit Anzahl der verlinkten Accounts und/oder benutzten Hashtags im Tweettext. \n')

#READER 
#Hiermit wird der Datensatz eingelesen und angezeigt. 
election = csv.reader(open("american-election-tweets.csv"), delimiter=';') #Datenimport
#Die Variable election wird erstellt und die DB dieser Variable zugeordnet. Trennzeichen ist das Semikolon
# Erzeugen einer leeren Liste Data 
data = []
print("Show me what you imported:")
for row in election:
    data.append(row) #Jede Zeile der DB wirdan die (noch) leere Liste Data "angeheftet".
Header = data[0] #Kennzeichnung, dass die erste Zeile als Header (Spaltenueberschriften) benutzt wird. Dies soll potentiell falsche Werte in kuenftigen Datenanalysen vorbeugen.
data.pop(0) #Der .pop(0) Befehl entfernt das 0.te Listenelemen = Header/Spaltenueberschriften.
print("Optimierte Darstellung:")
print (pd.DataFrame(data, columns=Header)) #Wir lassen uns hiermit die DB ausgeben. Panda macht dies visuell ansprechend und sehr simple. Die Spalten werden definiert ueber die Header.

#DATAINTEGRITY
# Hier wird überprüft, ob es im Datensatz problematische Leerzeichen gibt. Dies wird über eine einfache if-Bedingung durchgeführt.
print("Test auf Datenintegrität:")
if '\0' in open('american-election-tweets.csv').read():
    print ("Achtung, es befinden sich Null Bytes im Datensatz")
    reader = csv.reader(x.replace('\0', '') for x in 'american-election-tweets.csv') 
    #Oben wird der Null Value durch '' ersetzt. 
else: #Falls sich keine Leerzeichen im DAtensatz befinden, wird die else-Bedingung durchgeführt.
    print ("Es befinden sich keine (!) Null Bytes im Datensatz")
#Desweiteren wollen wir in der Spalte original_author alle Leerzellen durch den Eintrag "false" ersetzen
if '' in open('american-election-tweets.csv').read(r[3]):
    reader = csv.reader(x.replace('', 'False') for x in 'american-election-tweets.csv') 
    #Oben wird '' durch 'False' ersetzt. 
next.row

#DELETE COLUMNS
#Nun wollen wir unnoetige Spalten entfernen. Dies waren die Spalten [5] in reply to screen name, [6] is quote status, sowie [10] truncated. Dafuer ueberfuehren wir den Datensatz in ein neues "sauberes" CSV File 
with open("american-election-tweets.csv","rt") as source:
    rdr= csv.reader( source )
    with open("american-election-tweets_edit_v0.2.csv","wb") as result:
	      wtr= csv.writer( result )
        del r[5], r[6], r[10] #r[5] in reply to screen name; r[6] is quote status; r[10] truncated
        wtr.writerow( r )
	      for r in rdr:
        wtr.writerow( r[:4], r[7], r[8], r[9]) #Dies sind die Spalten, die wir aus der "alten" CSV-Datei uebernehmen wollen.

#REARRANGE/RE-ORGANIZE COLUMNS
#Zur besseren Uebersicht, wollen wir die Spalten 
df = pd.read_csv('american-election-tweets_edit_v0.2.csv')
 add this column to the end
df["TweetID"] = ""
cols = df.columns.tolist()
	 reorder columns:
cols = cols[:3] + [cols[-1]] + cols[3:13]
   "commit" the reordering
df = df[cols]
   write the output without Pandas' first index column
df.to_csv('american-election-tweets_edit_v0.2.csv', index=False)

with open('american-election-tweets.csv', 'r') as infile, open('american-election-tweets_edit_v0.1.csv', 'a') as outfile:
     output dict needs a list for new column ordering
    fieldnames = ['A', 'C', 'D', 'E', 'B']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
     reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
         writes the reordered rows to the new file
        writer.writerow(row)

#ADDNEWCOLUMS
#Zur spaeteren Analyse via SQL etc. versuchen wir Spalten einzufuegen mit zusaetzlichen Informationen oder bisherige Spalten zu parsen und auf mehrere aufzuteilen.
new_cols = [] # Platzhalter fuer neue Spalten

#1. TweetID (eine eindeutige Nummer. Diese wollen wir durch einfaches Durchzaehlen mittels eienr for-Schleife, die bis zum letzten Zeileneintrag laeuft, generieren.)
Header.append("TweetID") #Auch der Header muss erweitert werden. 
TweetID = 0
for TweetID in range(len(data)):
    print(TweetID)
  data[TweetID].append(TweetID)
print("Gib's mir Panda! Aber recht huebsch, bitte!")
print (pd.DataFrame(data, columns = Header))

#2. Sprachniveau
#Hier wollen wir das dictionary von http://pearsonpte.com/wp-content/uploads/2014/07/AcademicCollocationList.xls nutzen, um alle Woerter der Tweets (siehe in Spalte 'handle') abzugleichen und zu gucken, ob sich das Sprachvokabular der beiden PKandidaten unterscheidet und wenn ja, wer von beiden mehr matches mit dem academic english dict hat.
Header.append("AcadVocab")
new_cols = []
k = 0
matchcount = [k for k in parse(str).election(r[2]) if AcademicCollocationList.xls = election]
for k in samekeys:
	k = k + 1 
	print ("k")

for r[2] in election:     # For - Schleife, um alle handles 
	new_col = matchcount compare parse(r[2]).dict(AcademicCollocationList.xls, 2:4)
	new_row = row      # at first, just copy the row
	for key, value in changes.items(): # iterate over 'changes' dictionary
          # new_row = [ x.replace(key, value) for x in new_row ] # make the substitutions
        #new_rows.append(new_row) # add the modified rows
diffkeys = [k for k in dict1 if dict1[k] != dict2[k]]
for k in diffkeys:
  print k, ':', dict1[k], '->', dict2[k]

#3. Hashtags
Header.append("Hashtags") #Auch der Header muss erweitert werden. 
x = 1
for x in r[1]):
		parse.str('#')
		x = x + 1
    data[Hashtags].append(Hashtags)

#SORT For Specific Value
print('Sort Election by ColNr:') #Nun folgt ein Sortieralgorithmus, der im Funktionsmodul bereits enthalten gewesen ist.
with open('american-election-tweets_edit_v0.2.csv', newline='') as csvfile: #Import und Einlesen des Datensatzes
	election = csv.reader(csvfile, delimiter=';') 
	#Der eingelesene Datensatz erhaelt den Namen "election"; 
	#ACHTUNG: Trennzeichen (siehe delimiter) ist nicht standardgemaess ein Komma sondern ein Semikolon!
	sortedelection = sorted(election, key=operator.itemgetter(1), reverse=True)
	#Die Funktion sorted aus operator wird aufgerufen und der Variable "sortedelection" zugewiesen
	#election ist der Datensatz; key bezeichnet die Zielspalte, nach der sortiert wird; reversed=True bedeuted DESC Reihenfolge
	for TweetID, handle, text, is_retweeted, original_author, time_date, time_UTCtime, retweet_count, favorite_count, source_url, Len(word), Account_Mention1, Hashtag1 in sortedelection:
		#for schleife zum Durchforsten der Datei. Die Spalten werden hier benannt, damit die Sortierung richtig ist. Die Reihenfolge wird hier einfach eingefuegt. 
		print(TweetID, handle, text, is_retweeted, original_author, time_date, time_UTCtime, retweet_count, favorite_count, source_url, Len(word), Account_Mention1, Hashtag1)
	   
