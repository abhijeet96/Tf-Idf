# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:59:02 2017

.. module:: cosine_simil
   :platform: Windows
   :synopsis: deals with functions related to calculating cosine similarity, and returning top 10 results


@author: Abhijeet singh
"""
import math
import heapq
import pickle
song_score = pickle.load(open("song_score.p", "rb"))  #contains the sentiment score of each song


def calc_dist(val,query):
    """
    Calculates cosine similarity between given query and val: which is one particular tf-idf vector
    from the tf-idf matrix

    :param val: the tf-idf vector in consideration
    :type val: list
    :param query: the input query which is converted to a BoW->tf-idf vector
    :type query: list
    :returns: double -- cosine similarity value between val(one particular tf-idf vector) and query(input vector)
    """

    j=0    
    dist=0
    querysum=0;
    valsum=0
   
   #calculating cosine similarity score for tf-idf in list representation::
    for i in range(len(query)):
        while(j<len(val) and val[j][0]<query[i][0]):
            j+=1
        if(j==len(val)):
            break
        if(val[j][0]==query[i][0]):
            dist+=val[j][1]*query[i][1]
        
        
    for k in range(len(query)):
        querysum+=query[k][1]*query[k][1]
    
    for l in range(len(val)):
        valsum+=val[l][1]*val[l][1]
    
    querysum=querysum**(1/2.0)
    valsum=valsum**(1/2.0)
    
    return dist/(querysum*valsum)      
    
        


def similar(query):   
    """
    Prints top 10 matches for given query by user

    :param query: input string given by user
    :type query: string
    :returns : nothing


    """
    tf_idf=pickle.load(open("tf-idf.p", "rb"))
    
    song_map=pickle.load(open("song_map.p", "rb"))
    
    heap=[]
    
    for key,val in tf_idf.items():
        
        dist= calc_dist(val,query)
        heap.append([dist,key])
    
    heapq.heapify(heap)   # a heap is used to get the top 10 most similar matches. The time complexity reduces to O(klogn)    
    answer=heapq.nlargest(10,heap)
    
    answer_2=[]
    for i in answer:
        #print(song_map[i[1]],song_score[i[1]])
        answer_2.append([song_map[i[1]],song_score[i[1]],i[0]])

    answer_2.sort(key=lambda x: x[1])  
    
     
    for i in answer_2:
        print(i[0],i[2])
    
        
        
#similar([[2, 0.09711806593944841], [59, 0.5385669497585887], [262, 1.15903822760175], [300, 1.2366531186699423], [840, 2.0153565553732427]])