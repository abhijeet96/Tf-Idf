# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 15:47:55 2017

@author: Abhijeet singh
"""

import pickle

song_map={}

with open('mxm_779k_matches.txt','r',encoding='utf-8') as file:   
     try:
         for line in file:
             word_list=line.split('<SEP>')
             #print(word_list[0],word_list[1],word_list[2])
             song_map[word_list[0]]=(word_list[1],word_list[2])
             print(1)
     except UnicodeDecodeError:
                print ('error')

pickle.dump(song_map, open( "song_map.p", "wb" ) )