# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:49:57 2017

@author: abhijeet singh
"""

import pickle
import stemmer

senti_dict={}

with open('AFINN.txt','r') as file:
         for line in file:
             word_list=line.split('\t')
             #print(stem(word_list[0]),word_list[1].strip())
             senti_dict[stem(word_list[0])]=word_list[1].strip()

pickle.dump(senti_dict, open( "senti_dict.p", "wb" ) )