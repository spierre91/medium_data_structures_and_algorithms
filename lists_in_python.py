#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:02:28 2020

@author: sadrachpierre
"""

abbey_road = [("Come Together", "Lennon"), ("Something", "Harrison"), 
              ("Maxwell's Silver Hammer", "McCartney"), 
              ("Oh! Darling!","McCartney"), ("Octopus's Garden", "Starr"), 
              ("I Want You", "Lennon")]
#while loops
j = 0
while j < len(abbey_road):
    print(abbey_road[j]) 
    j+=1
    
#filtering with while loops     
j = 0
while j < len(abbey_road): 
    if abbey_road[j][1] != "McCartney":     
        print(abbey_road[j]) 
    j+=1

#for loops
for song, artist in abbey_road:
    print((song, artist))
    
#filtering with for loops   
for song, artist in abbey_road:
    if artist != "Lennon":
        print((song, artist))

#index-based for loops 
for i in range(len(abbey_road)):
    print((abbey_road[i][0], abbey_road[i][1]))
    
#filtering with index-based for loops 
for i in range(len(abbey_road)):
    if abbey_road[i][1] != "Harrison":
        print((abbey_road[i][0], abbey_road[i][1]))

#filtering with list comprehension 
filtered_list = [(song, artist) for song, artist in abbey_road if artist != "Lennon"]        
print(filtered_list)