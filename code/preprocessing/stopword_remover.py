#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove stopwords from the tokenized tweets

@author: meloezkan
"""

import ast

from code.preprocessing.preprocessor import Preprocessor
from nltk.corpus import stopwords

from code.util import COLUMN_STOPWORDS


class StopWords(Preprocessor):
    """Remove stop words from the tokenized words."""
    
    def __init__(self, input_column):
        """Initialize the Tokenizer with the given input and output column."""
        super().__init__([input_column], COLUMN_STOPWORDS)
    
    # don't need to implement _set_variables(), since no variables to set
    
    def _get_values(self, inputs):
        """Remove the stopwords"""
        
        clean_tweets = []

        # iterate over the pandas Series        
        for tweet in inputs[0]:

            # make sure tweet is tokenized
            assert tweet.startswith('[')
            assert tweet.endswith(']')

            tweet_token = ast.literal_eval(tweet)
            current_tweet = [token for token in tweet_token if token not in stopwords]
            
            clean_tweets.append(str(current_tweet))
        
        return clean_tweets