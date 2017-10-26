About the dataset:
-----------------
The Million Song Dataset (MSD) is a collection of metadata for a million popular music tracks produced by LabROSA in collaboration with The Echo Nest. A subset of this data, called the musicXmatch Dataset (MXMD), consists of 237,662 lyrics to songs within the MSD provided in a Bag-of-words format with the 5000 most common (stemmed) words. The dataset had two such datasets- one named train data and the other named test data.
Test data which had 27,143 songs was used as the corpus for this IR system.

Data description:
----------------
One sample data point:

TRAABRX12903CC4816,1548880,2:19,4:7,5:6,10:1,12:13,13:6,17:4,18:6,22:1,23:1,30:11,32:4,33:6,46:8,60:1,73:1,82:1,89:1,103:5,116:1,118:5,134:1,162:1,184:1,201:3,212:5,234:5,260:3,268:4,274:4,275:1,279:4,297:1,351:6,404:9,449:4,462:1,484:4,517:6,521:5,730:5,814:1,878:1,1003:10,1133:5,1649:7,2090:5,2258:1,2358:1,2740:4,3016:1,3024:1,3270:7,3741:9,4435:4

Track_id,word1_id:word1_count,word2_id:word2_count.........

The word_ids spanned from 1-5000. 
Along with the data file, There were:
- A text file containing Track_id: Artist name,Song name. This was read into a dictionary song_map
- A text file containg word_id:stemmed word. This was read into two dictionaries word_index and index_word and stored as pickle files


Methodology:
+++++++++++

TF-IDF was used for building this IR system. However to improve on the memory occupied and also the run time, a TF-IDF dictionary of lists was implemented.

Pre-processing:
--------------
- The given user query was first stemmed and case-corrected by the exact same stemming algorithm used by musiXmatch dataset. 
- Then, by iterating over index_word, the stemmed words in the query were converted to indexes. 
- Now, for each of these indexes, the count was calculted and converted to BoW model, sorted according to increasing index value.
- using the idf dictionary which was precomputed for each word-index, the query in BoW was converted to a tf-idf query

eg- input: Hello from the other side
	converts to : [[2, 0.09711806593944841], [59, 0.5385669497585887], [262, 1.15903822760175], [300, 1.2366531186699423], [840, 2.0153565553732427]]


Index Construction:
------------------

Since the data was already in a BoW model, it was converted to a tf-idf sparse matrix.

Tf-IdF matrix is a dictionary of lists of pairs with key:trackID and value:list

key: TRAABRX12903CC4816 | value :list | size of list: 55 | [[2, 0.22130814247709235], [4, 0.21737727701051068], [5, 0.22864546989795792], [10, 0.15869222215370163], [12,...

key: TRAADFO128F92E1E91 | value : list | size of list: 172 |[[1, 0.3881501109141686], [2, 0.2738286538511271], [3, 0.3354954265568886], [4, ...

and so on.


Information Retrieval:
--------------------

 - To calculate the cosine_similarity between the tf-idf query and the tf-idf, an iteration over the two lists was used which made the time complexity : O(m+n) per tf-idf vector where m=no. of distinct words in tf-idf list, n=number of distinct words in tf-idf query
 - An ordinary Tf-IDF matrix would be of the size 27143*5000, and per query, the time taken would have been O(5000*5000*27143)
 - However, using a dictionary of lists, the time complexity per query was brought down to O(m*n*27143), where m is on average around 66
 - the cosine similarity values for the whole matrix was stored in a list which was then converted to a heap, and the top 10 items were taken from this heap. Time complexity for this= O(klogn)  where k=10, n=27143

 So, per query the time complexity for retrieval is O(m*n*27143)+O(10log27143)


The precision and accuracy is subjective and can't be commented upon. However, looking at the lyrics of the top 10 tells us that it is correctly implemented.


Sometimes, we wouldn't know the exact lyrics in question and would want to search for the song, then ,it would make much more sense to search for the songs with respect to the sentiment levels. to incorporate this, sentiment analysis was used to sort the top 10 results according to sentiment.
AFINN sentiment data was used which assigned around 2700 words a sentiment score from +5 to -5. A sentiment score was calculated for each of the songs in question and the top 10 was then sorted with respect to that sentiment score. This was under the premise that the user's query would be too small to gauge the sentiment value and it would best left to the user to look for the sentiment value.
It was also thought that speech input would make a lot of sense as it is linked to looking for a song. Google's speech recognition API was used for this.


Data Structures Used:
--------------------
- Tf-idf: Dictionary of lists of pairs.  {'string':[[i1,i2],[i3,i4]],'string2':[[i5,i6],[i7,i8]]}
- word_index: Dictionary mapping integer to string {i1:'word1','i2':'word2'}
- index_word: Dictionary mapping string to integer
- heap: min heap for top 10 closest lyrics
- idf: Dictionary mapping integer to integer
- song_map: Dictionary mapping string to pair of strings (trackid to track_name and artist_name)
- query_input: List of pairs


The pickle library was used to make these Data structures persistent. All of the above mentioned strutures were saved as pickle files.
