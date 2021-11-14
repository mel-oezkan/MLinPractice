#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Utility file for collecting frequently used constants and helper functions.

Created on Wed Sep 29 10:50:36 2021

@author: lbechberger
"""

# column names for the original data frame
COLUMN_TWEET = "tweet"
COLUMN_LIKES = "likes_count"
COLUMN_RETWEETS = "retweets_count"

# column names of novel columns for preprocessing
COLUMN_LABEL = "label"
COLUMN_TIME = 'time'
COLUMN_PUNCTUATION = "tweet_no_punctuation"
COLUMN_LINKS = "tweet_no_links"
COLUMN_STOPWORDS = 'tweet_token_no_stop'

SUFFIX_TOKENIZED = "_tokenized"

# column names for feature extraction
TIME_FEATURE = 'TimeFeature'