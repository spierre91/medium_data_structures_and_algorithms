#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 12:12:35 2020

@author: sadrachpierre
"""

'''Defining Dictionaries'''

movie_ratings = {'movie_name': ['Parasite', 'Once Upon a Time in Hollywood', 'Marriage Story'], 'rating': [96, 83, 93]}
print(movie_ratings)

movie_ratings = {'movie_name': {'Parasite', 'Once Upon a Time in Hollywood', 'Marriage Story'}, 'rating': {96, 83, 93}}
print(movie_ratings)


'''Defining a list dictionary'''


from collections import defaultdict

movie_ratings = defaultdict(list)

movie_ratings['movie_name'].append('Parasite')
movie_ratings['movie_name'].append('Once Upon a Time in Hollywood')
movie_ratings['movie_name'].append('Marriage Story')

print(movie_ratings)


movie_ratings['rating'].append(96)
movie_ratings['rating'].append(83)
movie_ratings['rating'].append(93)

print(movie_ratings)


movie_ratings['movie_name'].append('Parasite')
movie_ratings['rating'].append(96)



print(movie_ratings)



'''Defining a set dictionary'''

movie_ratings = defaultdict(set)

movie_ratings['movie_name'].add('Parasite')
movie_ratings['movie_name'].add('Once Upon a Time in Hollywood')
movie_ratings['movie_name'].add('Marriage Story')

print(movie_ratings)


movie_ratings['rating'].add(96)
movie_ratings['rating'].add(83)
movie_ratings['rating'].add(93)

print(movie_ratings)


movie_ratings['movie_name'].add('Parasite')
movie_ratings['rating'].add(96)

print(movie_ratings)