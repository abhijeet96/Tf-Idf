# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 02:41:11 2017

@author: Sapna singh
"""

import pickle

with open('words_5k.txt','r') as file:
         for line in file:
             word_list=line.split(',')

index_word={}

for i in range(len(word_list)):
    index_word[word_list[i]]=i+1

print(index_word)
pickle.dump(index_word, open( "index_word.p", "wb" ) )