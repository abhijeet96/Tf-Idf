# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:50:26 2017

@author: Abhijeet singh
"""

"""
This script was used to construct tf-idf sparse matrix which is a dictionary of vector of pairs

Index Construction:
------------------

Since the data was already in a BoW model, it was converted to a tf-idf sparse matrix.

Tf-IdF matrix is a dictionary of lists of pairs with key:trackID and value:list

key: TRAABRX12903CC4816 | value :list | size of list: 55 | [[2, 0.22130814247709235], [4, 0.21737727701051068], [5, 0.22864546989795792], [10, 0.15869222215370163], [12,...

key: TRAADFO128F92E1E91 | value : list | size of list: 172 |[[1, 0.3881501109141686], [2, 0.2738286538511271], [3, 0.3354954265568886], [4, ...

and so on.
"""

import pickle
import math

word_index=pickle.load(open("word_index.p","rb"))  #stores index:word as pickle file

tf={}  #will store tf-idf at the end of this script

ct=0;

with open('mxm_dataset_test.txt','r',encoding='utf-8') as file:   #corpus
         for line in file:
             
             word_list=line.split(',')
             
             tf_list=[]
             
             for wrd in word_list[2:]:
                 
                 id_count=wrd.split(':')
                 id_x=int(id_count[0].strip())
                 count=int(id_count[1].strip())
                 tf_list.append([id_x,count])
                 
             tf[word_list[0]]=tf_list  #stores term frequency
             ct+=1
                         
             
N=ct   

    
dft= [0 for i in range(5001)]

# for calculating idf, populating dft as per the formula
for i in range(1,5001):
    count_i=0
    for key,val in tf.items():         
        for words in val:
            if(words[0]==i):
                count_i+=1
    dft[i]=count_i
    
    
idft= [math.log10((N*1.0)/i) if i!=0 else 0 for i in dft]

pickle.dump(idft, open( "idft.p", "wb" ) )  #idft dumped as pickle file
            
#print(idft)

for key,val in tf.items():
    for words in val:
       words[1]=((1+math.log10(words[1]))*idft[words[0]])

#print(tf)


#pickle.dump(tf, open( "tf-idf.p", "wb" ) )
            
             

