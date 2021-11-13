#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to encode the time of the day 
in which the tweet was created. 

@author: meloezkan
"""


from sklearn.preprocessing import OneHotEncoder

from code.feature_extraction.feature_extractor import FeatureExtractor

class TimeFeature(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], "TimeFeature")
    
    def _set_variables(self, inputs):

        self.morning = 7 
        self.afternoon = 11
        self.noon = 15
        self.evening = 18
        self.night = 24

        # create one hot encoder and fit to times
        self.oneHot = OneHotEncoder(sparse=False)
        self.oneHot.fit([0,1,2,3])

    def _get_values(self, inputs):
        data = inputs[0]

        # assign the repsective value for the time
        time_values = None

        # convert the values into encodings
        self.oneHot.transform(time_values)