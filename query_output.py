# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:10:46 2017

@author: Abhijeet singh
"""

import pickle
import math
import cosine_simil
import lyrics_bow


def final_output(input_string):

    """
    Takes input as input_string given by the user. Converts it to BoW model using.lyrics_to_bow, calls .similar which prints top 10 results

    param input_string: takes input string as typed by user
    type input_string: string
    returns: nothing
    """

    convert_this=lyrics_bow.lyrics_to_bow(input_string)
        
    index_word = pickle.load(open("index_word.p", "rb"))
    
    query_input=[]
    
    #converts the stemmed BoW to word indexes. each of the 5000 words is given an index stores in the dictionary index_word
    for key,val in convert_this.items():    
        if key in index_word:   #converts words to indexes 1-5000
            query_input.append([index_word[key],val])   #index,frequency
    
    query=sorted(query_input, key=lambda x: x[0])  #sorted BOW according to the word indexes
    
    idft= pickle.load(open("idft.p", "rb"))  #contains inverse document frequency for 5000 word indices
    
    
    for words in query:
            words[1]=((1+math.log10(words[1]))*idft[words[0]]) #converting user input to tf-idf input vector
    
    cosine_simil.similar(query)  #checks cosine similarity between user query and all vectors in tf-idf matrix
    
    

#final_output("hello from the other side")


