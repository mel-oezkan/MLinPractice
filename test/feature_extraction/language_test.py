#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:51:00 2021

@author: mel-oezkan
"""

import unittest
import pandas as pd
import tempfile

from sklearn.preprocessing import OneHotEncoder

from code.feature_extraction.language_feature import LanguageFeature


class LanguageTest(unittest.TestCase):
    """ Testing the language feature. To create the encodings
    of the languages we need a sourcefile. For that using a temp
    file shoud suffice 
    """

    def setUp(self):
        self.INPUT_COLUMN = 'language'
        self.data = ['en', "de", "fr", "sp"]

        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = self.data

        self.temp_file = tempfile.NamedTemporaryFile(suffix=".csv")
        self.df.to_csv(self.temp_file.name)

        self.language_feature = LanguageFeature(self.temp_file)

    def test_column_name(self):

        # create the encodings using sklearn
        oneHot = OneHotEncoder(sparse=False)
        oneHot.fit([[x] for x in self.data])

        base_encodings = oneHot.transform(self.data)

        # create encodings with feature class
        feature_encodings = self.language_feature.fit_transform(self.df)

        print(base_encodings)
        print(feature_encodings)

        self.assertEqual(base_encodings, feature_encodings)

    def test_encodings(self):
        """Chek if the generated encodings equalt the 
        onece which should have been generated """

        pass


if __name__ == '__main__':
    unittest.main()
