# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 00:08:57 2017
Python 3.6
@author: Eike Sommer, Thomas Sieron, Christian Kujath
"""

import csv

with open('Id-Accounts-Hashtags-TextTEST.csv', 'wt', encoding="utf8", newline='') as outputFile:
    writer = csv.writer(outputFile, delimiter=";")
    writer.writerow(('TweetID', 'Erwähnte Accounts', 'Hashtags', 'Text')) # the header
    # american-election-tweets is sadly not in utf8 ?!? But it works this way, so...
    with open('american-election-tweets.csv', 'rt') as inputFile:
        reader = csv.reader(inputFile, delimiter=';')
        tweetID = 0 # start this counter
        
        header = next(reader) # so we start in 2nd row, not in the header
        for row in reader:
            tweetID = tweetID +1
            
            # get the indices of all @ and # characters:
            # (by making pairs of all characters in a tweet and their position, 
            # ie "Tweet" gives [(0,T),(1,w),(2,e)....])
            tweet=row[1]
            accountInds = [posi for (posi, chara) in enumerate(tweet) if chara == '@'] 
            tagInds = [posi for (posi, chara) in enumerate(tweet) if chara == '#']          
            # accounts and hashtags have no punctuation:
            #endChars = (' ', '.', ':', ';', ',', '\'','-','?','!','´','’','\n','…','"')
            # but now we just use .isalnum()
            
            # Now, find all account handles:
            accounts = []
            if len(accountInds) > 0:
                
                for i in accountInds:
                    j=1
                    while (tweet[i+j].isalnum()) | (tweet[i+j] == "_"): 
                        j=j+1
                        if (i+j == len(tweet)):
                            break

                    if j > 1:   # filter out @'s without account handles
                        accounts=accounts+[tweet[i:i+j]]
                        
            # Now do it for the tags:            
            tags=[]    
            if len(tagInds) > 0:
                
                for i in tagInds:
                    j=1
                    while  (tweet[i+j].isalnum()) | (tweet[i+j] == "_"):        
                        j=j+1
                        if (i+j == len(tweet)):
                            break
                    if j > 1:   # filter out empty hashtags from like "# ISIS"
                        tags=tags+[tweet[i:i+j]]

            writer.writerow((tweetID, accounts, tags, tweet))
print('Feddich!!!')
