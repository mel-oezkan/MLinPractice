#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collects the feature values from many different feature extractors.

Created on Wed Sep 29 12:36:01 2021

@author: meloezkan
"""

import numpy as np
from code.feature_extraction.feature_extractor import FeatureExtractor


class DataFeatures(FeatureExtractor):

    def __init__(self, input_column):
        # names the input column the same way was in the data
        super().__init__([input_column], input_column)

    def _set_variables(self, inputs):

        overall_text = []
        for line in inputs:
            tokens = ast.literal_eval(line.item())
            overall_text += tokens

        self._bigrams = nltk.bigrams(overall_text)
