# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:00:30 2017

@author: Abhijeet Singh
"""

senti_dict = pickle.load(open("senti_dict.p", "rb"))
word_index= pickle.load(open("word_index.p", "rb"))
tf_idf=pickle.load(open("tf-idf.p", "rb"))

song_score={}

for key,val in tf_idf.items():
    score=0
    denominator=0
    
    for j in val:
        #print(j)
        if(word_index[j[0]] in senti_dict):
            score+=float(j[1])*float(senti_dict[word_index[j[0]]])
            #print(float(senti_dict[word_index[j[0]]]))
            denominator+=float(j[1])
    
    if(denominator==0):
        song_score[key]=0
    else:
        song_score[key]=score/denominator
    
pickle.dump(song_score, open( "song_score.p", "wb" ) )
    
            
