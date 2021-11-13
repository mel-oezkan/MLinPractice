#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: meloezkan
"""

import unittest
import pandas as pd

from code.feature_extraction.timeFeature import TimeFeature

class TimeFeatureTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "time"
        
        # creat dataframe and fill with sample data
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = [
            '07:00:00', '08:00:00', '09:00:00' # morning samples
            '11:00:00', '12:00:00', '13:00:00' # afternoon samples
            '15:15:00', '16:16:00', '17:17:00' # noon samples
            '18:18:00', '19:19:00', '20:20:00' # evening samples
            '00:00:10', '01:01:00', '02:02:00' # night samples
        ]

        # initalize class 
        self.time_encoder = TimeFeature(self.INPUT_COLUMN)
        self.encodings = self.time_encoder.fit_transform(self.df)


    def test_input_columns(self):
        # checks if the input column is set correctly
        self.assertEqual(self.time_encoder._input_columns, [self.INPUT_COLUMN])

    def test_output_shape(self):
        # checks if the transofmation yields the expected shape of 
        # 15 examplex x 5 one hot encoding
        self.assertEqual(self.encodings.shape, (15,5))

    def test_output_encodings(self):
        # checks if the indices are set correctly
        self.assertEqual(self.encodings[ 0: 3].nonzero(), [0,0,0]) # morning
        self.assertEqual(self.encodings[ 3: 6].nonzero(), [1,1,1]) # afternoon
        self.assertEqual(self.encodings[ 6: 9].nonzero(), [2,2,2]) # noon
        self.assertEqual(self.encodings[ 9:12].nonzero(), [3,3,3]) # evening
        self.assertEqual(self.encodings[12:15].nonzero(), [4,4,4]) # night

