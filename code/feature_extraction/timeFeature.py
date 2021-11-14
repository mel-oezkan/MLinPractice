#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to encode the time of the day 
in which the tweet was created. 

@author: meloezkan
"""

from datetime import time 
import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder

from code.feature_extraction.feature_extractor import FeatureExtractor
from code.util import TIME_FEATURE

class TimeFeature(FeatureExtractor):
    
    
    def __init__(self, input_column):
        super().__init__([input_column], TIME_FEATURE)
    
    def _set_variables(self, inputs):

        self.morning = time(7)
        self.afternoon = time(11)
        self.noon = time(15)
        self.evening = time(18)
        # to check if smaller than night an itermediate
        # variable is needed since 19 < 0 -> false
        self.midnight = time(23, 59, 59)
        self.night = time(0)

        # create one hot encoder and fit to times
        self.oneHot = OneHotEncoder(sparse=False)
        self.oneHot.fit([[0],[1],[2],[3]])

    def _get_values(self, inputs):
        time_data = pd.to_datetime(inputs[0]).dt.time
        time_classes = np.zeros((time_data.size, 1))
        
        time_classes[np.logical_and(
            (time_data >= self.morning).tolist(), 
            (time_data < self.afternoon).tolist())] = 0

        time_classes[np.logical_and(
            (time_data >= self.afternoon).tolist(), 
            (time_data < self.noon).tolist())] = 1

        time_classes[np.logical_and(
            (time_data >= self.noon).tolist(), 
            (time_data < self.evening).tolist())] = 2

        time_classes[np.logical_and(
            (time_data >= self.evening).tolist(), 
            (time_data <= self.midnight).tolist())] = 3

        time_classes[np.logical_and(
            (time_data >= self.night).tolist(), 
            (time_data < self.morning).tolist())] = 4

        # convert the values into encodings
        self.oneHot.transform(time_classes)