# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:33:14 2017

@author: Abhijeet singh
"""

import pickle

with open('words_5k.txt','r') as file:
         for line in file:
             word_list=line.split(',')

word_index={}

for i in range(len(word_list)):
    word_index[i+1]=word_list[i]

pickle.dump(word_index, open( "word_index.p", "wb" ) )