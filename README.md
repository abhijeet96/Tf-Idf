Tf-idf on Musix dataset

The Pickle files folder contains scripts to calculate various persistent data structures-

•	Tf-idf: Dictionary of lists of pairs.  {'string':[[i1,i2],[i3,i4]],'string2':[[i5,i6],[i7,i8]]}

•	word_index: Dictionary mapping integer to string {i1:'word1','i2':'word2'}

•	index_word: Dictionary mapping string to integer

•	heap: min heap for top 10 closest lyrics

•	idf: Dictionary mapping integer to integer

•	song_map: Dictionary mapping string to pair of strings (trackid to track_name and artist_name)

•	query_input: List of pairs

For speech input, compile and run spttxt.py
For typed input, compile and run runtime.py
