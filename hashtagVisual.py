# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 17:30:42 2017

@author: Eike Sommer, Thomas Sieron, Christian Kujath
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
import kMeansAlgorithm as kMA

authors=[]
with open('american-election-tweets.csv', 'rt') as inputFile:
    reader = csv.reader(inputFile, delimiter=';')
    
    header = next(reader) # so we start in 2nd row, not in the header
    groupedTags=[]
    for row in reader:
        tweet=row[1]        
        tagInds = [posi for (posi, chara) in enumerate(tweet) if chara == '#']
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
                    groupedTags.append(tags)
                    
                    if row[0] == 'HillaryClinton':
                        authors.append('C')
                    else:
                        authors.append('D')
                    
groupedTagsCLIN=[]
groupedTagsTRUM=[]

for i in list(zip(groupedTags,authors)):
    if i[1] == 'C':
        groupedTagsCLIN.append(i[0])
    else:
        groupedTagsTRUM.append(i[0])
print('Clinton : Trump', len(groupedTagsCLIN), len(groupedTagsTRUM))

flatTagsCLIN=[item for sublist in groupedTagsCLIN for item in sublist]    
flatTagsTRUM=[item for sublist in groupedTagsTRUM for item in sublist]

hashtagListCLIN=set(flatTagsCLIN)
hashtagListTRUM=set(flatTagsTRUM)

freqCLIN=[]
freqTRUM=[]
for h in hashtagListCLIN:
    freqCLIN.append((h,flatTagsCLIN.count(h)))
    
for h in hashtagListTRUM:
    freqTRUM.append([h,flatTagsTRUM.count(h)])


coordsCLIN=[]
coordsTRUM=[]
for i in range(max(list(zip(*freqCLIN))[1])+1):
    xCoord=0
    for j in freqCLIN:
        if j[1] == i:
            coordsCLIN.append((xCoord,i))
            xCoord = xCoord+1
for i in range(max(list(zip(*freqTRUM))[1])+5):
    xCoord=0
    for j in freqTRUM:
        if j[1] == i:
            coordsTRUM.append((xCoord,i))
            xCoord = xCoord+1

mostUsedTagCLIN = freqCLIN[np.argmax(list(zip(*freqCLIN))[1])]
mostUsedTagTRUM = freqTRUM[np.argmax(list(zip(*freqTRUM))[1])]

aOC=4 # amount of clusters
threshold=0.01        
clusterCLIN=kMA.kMeansAlgo(aOC, coordsCLIN,threshold)
clusterTRUM=kMA.kMeansAlgo(aOC, coordsTRUM,threshold)
      
 
titleString='Wie oft wurden Hashtags von den Kandidaten benutzt?'
fig=plt.figure("k means algorithm" ,figsize=(19,12))
fig.suptitle(titleString, fontsize=16)

plot1 = fig.add_subplot(121)
plot1.margins(0.05, 0.05) 
plot1.set_title("Clinton")
plt.xlabel('Anzahl der Hashtags')
plt.ylabel('Haeufigkeit eines Hashtags')
kMA.plotKMeans(clusterCLIN[0],clusterCLIN[1],plt)  
plot1.text(5, mostUsedTagCLIN[1], mostUsedTagCLIN[0])   

plot2 = fig.add_subplot(122,sharex=plot1, sharey=plot1)
plot2.margins(0.05, 0.05) 
plot2.set_title("Trump")   
kMA.plotKMeans(clusterTRUM[0],clusterTRUM[1],plt)     
plot2.text(5, mostUsedTagTRUM[1], mostUsedTagTRUM[0])   

