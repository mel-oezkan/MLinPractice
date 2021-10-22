#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preprocessor that removes punctuation from the original tweet text.

Created on Wed Sep 29 09:45:56 2021

@author: mel-oezkan
"""

from code.preprocessing.preprocessor import Preprocessor
from code.util import COLUMN_TWEET, COLUMN_SENTIMENT

from nltk.sentiment import SentimentIntensityAnalyzer

# adds the sentiment of the tweet using a pretrained model
# of the nltk library


class SentimentAnalyzer(Preprocessor):

    # constructor
    def __init__(self):
        # input column "tweet", new output column
        super().__init__([COLUMN_TWEET], COLUMN_SENTIMENT)

    # set internal variables based on input columns
    def _set_variables(self, inputs):
        # store punctuation for later reference
        self.analyzer = SentimentIntensityAnalyzer()

    # get preprocessed column based on data frame and internal variables
    def _get_values(self, inputs):
        """Get the polar sentiment of the tweets"""

        polar_sentiment = []

        for tweet in inputs[0]:
            # the polarity score contains a value for
            # pos, neg, neutral and compound scores
            # for simplicity we will only use the compound score
            polar_sentiment.append(
                self.analyzer.polarity_scores(tweet)["compound"])

        return polar_sentiment
