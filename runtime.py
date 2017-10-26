# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:42:14 2017

@author: Abhijeet Singh

"""
import query_output
import time

lyrics = input("Enter lyrics: ") 


start = time.time()
query_output.final_output(lyrics)
print ('It took', time.time()-start, 'seconds.',len(lyrics.split(" ")))