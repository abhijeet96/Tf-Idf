# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:32:45 2017

@author: Abhijeet Singh
"""

#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
import query_output

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    query_string=r.recognize_google(audio)
    print("You said: " + query_string )
    query_output.final_output(query_string)   #calls final_output which gives o/p. rest of the code is for the google speech to text api 
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
