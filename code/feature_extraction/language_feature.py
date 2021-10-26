#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creates one hot encodings for the different languages

@author: meloezkan
"""

import numpy as np
from sklearn.preprocessing import OneHotEncoder

from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the character-based length as a feature


class LanguageFeature(FeatureExtractor):

    # constructor
    def __init__(self):
        super().__init__(['language'], "language_encoding")

    # takes the inputs and fetches the unique country count
    def _set_variables(self, inputs):

        uniqe_elems = set(inputs)
        self.oneHot = OneHotEncoder(sparse=False)

        # create the embeding scheme by fitting
        self.oneHot.fit([[x] for x in uniqe_elems])

    def _get_values(self, inputs):
        # create the encodings by applying transformation
        return self.oneHot.transform(inputs)
