# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:17:19 2017
Uses Python 3.6
@author: Eike Sommer, Thomas Sieron, Christian Kujath
"""
import numpy as np
np.set_printoptions(threshold=1000) # print any length of np.arrays
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

def eukDistArray(x,y): # x and y are two lists of 2-tuples/lists, 
# this gives the distance betweee each pair of  points :
    diff = np.array(x)-np.array(y)
    return np.sqrt(np.sum(np.array(list(zip(*diff**2))),axis = 0))

def getCentroid(points): # points list of tuples/lists, calculates their centroid:
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    return (sum(x) / len(points), sum(y) / len(points))
   
def plotKMeans(centroids,pointsSortedByClusters,picNumber): # picNumber = plot1,plot2 oder plt
    # color map stuff:
    k=len(centroids)
    start = 0.0 # begin with first color
    stop = 1.0  # and end with last color in the map
    numberOfColors= k
    colorSelection = np.linspace(start, stop, numberOfColors)
    colors = [mpl.cm.gist_rainbow(cS) for cS in colorSelection]
       
    for i in range(k):
        temp=list(zip(*pointsSortedByClusters[i]))

        picNumber.plot(temp[0], temp[1],'.', markerfacecolor=colors[i], markeredgecolor=colors[i])
        picNumber.plot(centroids[i][0],centroids[i][1],'s', markerfacecolor=colors[i], markeredgecolor='black')

# Main algorithm:
def kMeansAlgo(centroids, points, threshold):
    # for quick testing threshold should be near 1, otherwise closer to zero, like 0.05
    # points is a list of 2-tuples/lists of points
    # centroids is a list of starting points for the centers or an int, then the 
    # algorithm chooses that many at random:
    if type(centroids) == int: # (so if just the amount of clusters we want, not actual start points for clusters)
        k=centroids
        randStartInds=random.sample(range(len(points)),k)
        centroids=list(points[c] for c in randStartInds)
    else:
        k=len(centroids)
    
    oldCentroids = [(0,0)]*k
    newCentroids = centroids 
    
    iterCount = 0
    iterCountMax = 1000 # second kill switch
    
    while ((iterCount < iterCountMax) and (max(eukDistArray(oldCentroids,newCentroids))) > threshold):
        # those print outs are only for testing
    #    print('Iteration: ', iterCount)
    #    print('max distance between old and new centroids: ', max(eukDistArray(oldCentroids,newCentroids)))
        
        oldCentroids = newCentroids
        [newCentroids,sortedPoints]= innerLoopKMA(newCentroids, points)
        iterCount=iterCount+1
        # use this first plot here only for testing:
     #   if iterCount == 1 :
     #       plotKMeans(oldCentroids,sortedPoints,plot1)
                
 #   plotKMeans(newCentroids,sortedPoints,plot2) # plots the last step, maybe comment out later  
    return [newCentroids, sortedPoints]

# main loop of main algorithm:
def innerLoopKMA(centroids, points): # of the main algorithm
    PointsWithCentroids=[]
    k=len(centroids)
    for p in points:  
        indexMin=np.argmin(eukDistArray([p]*k,centroids))
        PointsWithCentroids.append([p,indexMin])      
        
    pointsSortedByClusters=[[] for _ in range(k)]
    for p in PointsWithCentroids:
        pointsSortedByClusters[p[1]].append(p[0])
    
    newCentroids=[]
    for i in range(k): 
        newCentroids.append(getCentroid(pointsSortedByClusters[i]))    
    return [newCentroids, pointsSortedByClusters]        
     
# =============== testing stuff: ===========================================
# create random points for testing:
x=[]
y=[]
for i in range(8000):
    x.append(random.randint(-100,100))
    y.append(random.randint(-100,100))

# how many clusters do you want:
clusters=8

#plot stuff:
'''
titleString='k means algorithm with random numbers and '+ str(clusters) + " clusters"
fig=plt.figure("k means algorithm" ,figsize=(19,12))
fig.suptitle(titleString, fontsize=16)

plot1 = fig.add_subplot(121)
plot1.margins(0.05, 0.05) 
plot1.set_title("After the first step")

plot2 = fig.add_subplot(122,sharex=plot1, sharey=plot1)
plot2.margins(0.05, 0.05) 
plot2.set_title("After the final step")       
'''
# call the algorithm:
#kMeansAlgo(clusters,list(zip(x,y)),1)




    




