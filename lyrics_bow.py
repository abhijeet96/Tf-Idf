# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 01:56:10 2017

@author: Abhijeet singh
"""
import stemmer

"""
uses the stem function and converts lyrics to bag of words.
the MusiXmatch dataset has selected 5000 words deemed worthy to feature in the BoW model.
The user input is also converted to BoW format by making use of this function
"""


def lyrics_to_bow(lyrics):
    """
    Main function to stem and create bag of words.
    It is what was used for the musiXmatch dataset.    .
    
    :param lyrics: song lyrics to be formatted
    :type lyrics:string
    
    :returns:dictionary word -> count or None if something was wrong (e.g. not enough words)
    """
    # remove end of lines
    lyrics_flat = lyrics.replace('\r', '\n').replace('\n', ' ').lower()
    lyrics_flat = ' ' + lyrics_flat + ' '
    # special cases (English...)
    lyrics_flat = lyrics_flat.replace("'m ", " am ")
    lyrics_flat = lyrics_flat.replace("'re ", " are ")
    lyrics_flat = lyrics_flat.replace("'ve ", " have ")
    lyrics_flat = lyrics_flat.replace("'d ", " would ")
    lyrics_flat = lyrics_flat.replace("'ll ", " will ")
    lyrics_flat = lyrics_flat.replace(" he's ", " he is ")
    lyrics_flat = lyrics_flat.replace(" she's ", " she is ")
    lyrics_flat = lyrics_flat.replace(" it's ", " it is ")
    lyrics_flat = lyrics_flat.replace(" ain't ", " is not ")
    lyrics_flat = lyrics_flat.replace("n't ", " not ")
    lyrics_flat = lyrics_flat.replace("'s ", " ")
    # remove boring punctuation and weird signs
    punctuation = (',', "'", '"', ",", ';', ':', '.', '?', '!', '(', ')',
                   '{', '}', '/', '\\', '_', '|', '-', '@', '#', '*')
    for p in punctuation:
        lyrics_flat = lyrics_flat.replace(p, '')    
    
    
    words = [i for i in lyrics_flat.split(' ')]    
    
    # stem words
    words = map(lambda x: stemmer.stem(x), words)
    bow = {}
    for w in words:
        if not w in bow.keys():
            bow[w] = 1
        else:
            bow[w] += 1
    # remove special words that are wrong
    fake_words = ('>', '<', 'outro~')
    bowwords = bow.keys()
    for bw in bowwords:
        if bw in fake_words:
            bow.pop(bw)
        elif bw.find(']') >= 0:
            bow.pop(bw)
        elif bw.find('[') >= 0:
            bow.pop(bw)
    # not big enough? remove instrumental ones among others
    if len(bow) <= 3:
        return None
    # done
    return bow



