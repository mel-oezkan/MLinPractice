#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:51:00 2021

@author: mel-oezkan
"""

import unittest
import pandas as pd
import nltk
from code.feature_extraction.bigrams import BigramFeature


class LanguageTest(unittest.TestCase):

    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.language_feature = None
        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = [
            'en', "de", "fr", "sp"
        ]

    def test_input_columns(self):
        self.assertEqual()

    def test_feature_name(self):
        self.assertEqual(self.language_feature.get_feature_name(),
                         self.INPUT_COLUMN + "_bigrams")

    def test_created_encodings(self):
        self.language_feature.fit(self.df)
        # modify to fit the requirements


if __name__ == '__main__':
    unittest.main()
