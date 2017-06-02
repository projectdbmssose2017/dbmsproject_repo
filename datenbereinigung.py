#DBS: Projektgruppe 42 IterationII Datenbereinigung via Python 
#https://stackoverflow.com/questions/14471049/python-2-7-1-how-to-open-edit-and-close-a-csv-file
#https://docs.python.org/3.5/library/csv.html

import csv # learn more: https://python.org/pypi/csv Funktion zum Bearbeiten von CSV Dateien
import operator #Funktionsmodul fuer standardoperatoren (e.g., add)
#import pandas as pd #Funktionsmodul fuer rearrange und addnewcolumn
print('Folgendermaßen sind die Attribute des Datensatzes american-election-tweets.csv (DB "Election") geordnet: (Spaltennummer) Spaltenname \n \n (0) TweetID, (1) handle, (2) text, (3) is_retweeted, (4) original_author, (5) time_date, (6) time_UTCtime, (7) retweet_count, (8) favorite_count, (9) source_url, (10) Len(word), (11) Account_Mention1, (12) Hashtag1, (n) HashtagN / Account_MentionN \n \n Hinweis: Die Spaltenanzahl variiert mit Anzahl der verlinkten Accounts und/oder benutzten Hashtags im Tweettext. \n')

#DATAINTEGRITY
#open('american-election-tweets.csv').read().index('\0')
print("Test auf Datenintegrität:")
if '\0' in open('american-election-tweets.csv').read():
    print ("Es befinden sich Null Bytes im Datensatz")
    reader = csv.reader(x.replace('\0', '') for x in 'american-election-tweets.csv')
else:
    print ("Es befinden sich keine (!) Null Bytes im Datensatz")

#READER 
with open('american-election-tweets.csv', newline='') as csvfile:
	election = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in election:
			print (', '.join(row))

#DELETE COLUMNS


with open("american-election-tweets.csv","rt") as source:
    rdr= csv.reader( source )
    with open("american-election-tweets_edit_v0.2.csv","wb") as result:
        wtr= csv.writer( result )
#        del r[5], r[6], r[10] #r[5] in reply to screen name; r[6] is quote status; r[10] truncated
#        wtr.writerow( r )
        for r in rdr:
            wtr.writerow( r[1], r[2])

#REARRANGE/RE-ORGANIZE COLUMNS
#df = pd.read_csv('american-election-tweets.csv')
# add this column to the end
#df["TweetID"] = ""
#cols = df.columns.tolist()
	# reorder columns:
#cols = cols[:3] + [cols[-1]] + cols[3:13]
  # "commit" the reordering
#df = df[cols]
  # write the output without Pandas' first index column
#df.to_csv('american-election-tweets_edit_v0.1.csv', index=False)

#with open('american-election-tweets.csv', 'r') as infile, open('american-election-tweets_edit_v0.1.csv', 'a') as outfile:
    # output dict needs a list for new column ordering
#    fieldnames = ['A', 'C', 'D', 'E', 'B']
#    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
#    writer.writeheader()
#    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
#        writer.writerow(row)

#ADDNEWCOLUMS
#new_rows = [] # a holder for our modified rows when we make them
#changes = {   # a dictionary of changes to make, find 'key' substitue with 'value'
    #'1 dozen' : '12', # I assume both 'key' and 'value' are strings
    #}

#with open('test.csv', 'rb') as f:
    #reader = csv.reader(f) # pass the file to our csv reader
    #for row in reader:     # iterate over the rows in the file
        #new_row = row      # at first, just copy the row
        #for key, value in changes.items(): # iterate over 'changes' dictionary
          # new_row = [ x.replace(key, value) for x in new_row ] # make the substitutions
        #new_rows.append(new_row) # add the modified rows

#with open('test.csv', 'wb') as f:
    # Overwrite the old file with the modified rows
    #writer = csv.writer(f)
    #writer.writerows(new_rows)


#SORT For Specific Value
#print('Sort Election by ColNr:') #Nun folgt ein Sortieralgorithmus, der im Funktionsmodul bereits enthalten gewesen ist.
#with open('american-election-tweets.csv', newline='') as csvfile: #Import und Einlesen des Datensatzes
	#election = csv.reader(csvfile, delimiter=';') 
	#Der eingelesene Datensatz erhaelt den Namen "election"; 
	#ACHTUNG: Trennzeichen (siehe delimiter) ist nicht standardgemaess ein Komma sondern ein Semikolon!
	#sortedelection = sorted(election, key=operator.itemgetter(1), reverse=True)
	#Die Funktion sorted aus operator wird aufgerufen und der Variable "sortedelection" zugewiesen
	#election ist der Datensatz; key bezeichnet die Zielspalte, nach der sortiert wird; reversed=True bedeuted DESC Reihenfolge
	#for TweetID, handle, text, is_retweeted, original_author, time_date, time_UTCtime, retweet_count, favorite_count, source_url, Len(word), Account_Mention1, Hashtag1 in sortedelection:
		#for schleife zum Durchforsten der Datei. Die Spalten werden hier benannt, damit die Sortierung richtig ist. Die Reihenfolge wird hier einfach eingefuegt. 
		#print(TweetID, handle, text, is_retweeted, original_author, time_date, time_UTCtime, retweet_count, favorite_count, source_url, Len(word), Account_Mention1, Hashtag1)
	    
	    
