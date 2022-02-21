# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 14:43:12 2021

@author: srpdo
"""

import numpy as np

def mean(a_list):
    #calculates the mean of the given data
    total = 0                               
    
    n_data = len(a_list)
    
    for i in range(n_data):
        
        total += a_list[i]          #sums up all the data in the set
        
    return total/n_data             #returns the sum of all data divided by the number of them


def median(a_list):
    #finds the median value of the give list, works only for even numbered lists
    
    a_list = np.sort(a_list)            #sorting the list in an increasing manner
    n_data = len(a_list)                
    median = a_list[int(n_data/2)]      #finds the data in the middle
        
    return median                       #returns the median




def std(a_list):
    #calculates the standart deviation of the given list
    
    mu = mean(a_list)
    n_data = len(a_list)
    dist_sq = 0
    
    for i in range(n_data):
        dist_sq += (a_list[i] - mu)**2          #sums up the square of differences between mean of the data with each data point
        
    lin_dist = (dist_sq/(n_data-1))**(0.5)        #dividing the sum into the number of entries and taking the square root
    
    return lin_dist                             #returns the standart deviation
    


def skew(a_list):
    #decides if the skew is positive or negative 
    
    if mean(a_list) - median(a_list) > 0:
        return("+")                             #returns + if the mean of the data set is greated than its median
    elif mean(a_list) - median(a_list) < 0:
        return("-")                             #returns - if the media of the data set is greated than its mean
    else:
        return 0                                #returns zero if the data is perfectly symmetric

    
titles=["mt1","mt2","fin","lab","hw","Att."]                        #titles of the collums
calc =["mean", "median", "standart deviation", "skew" ]             #will be used in printing, practical reasons only

f=open("data2_1.txt","r")                 #opening the txt file in reading mode

data =  np.loadtxt("data2_1.txt")         #takes the columns from the data

f.close()

data = data.T                           #transpose the data so that every column creates a line in the list

#print(data)

means = []                              #will hold the means of the columns
medians = []                            #will hold the meadians of the columns
stds = []                               #will hold the standart deviations of the columns
skews = []                              #will hold the directions of skews of the columns (+/-)

for i in range(len(data)):              #filling each list accordingly
    means.append(mean(data[i]))
    stds.append(std(data[i]))
    medians.append(median(data[i]))
    skews.append(skew(data[i]))
    
    
data_0 =[means,medians,stds,skews]      #all datas at one place for easy printing


for i in range(len(titles)):            #prints the titles of the rows with the name of the calculations at once
    for j in range(len(calc)):
        
        print(titles[i], calc[j], " is ", data_0[j][i])

