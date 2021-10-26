#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creates one hot encodings for the different languages

@author: meloezkan
"""

from os import path
import numpy as np
import pandas as pd
import pathlib
from sklearn.preprocessing import OneHotEncoder

from code.feature_extraction.feature_extractor import FeatureExtractor

# class for extracting the character-based length as a feature


class LanguageFeature(FeatureExtractor):

    # constructor
    def __init__(self, source_file):
        super().__init__(['language'], "language_encoding")

        self.source = source_file
        self.source_file = pathlib.Path(self.source_file)
    # takes the inputs and fetches the unique country count

    def _set_variables(self, inputs):

        # check the source file befor using
        assert self.source_file.exists(), (
            "Given Source file does not exits")
        assert self.source_file.suffix == "csv", (
            "Given source file has to be a csv")

        # read the file and fetch the language column
        data = pd.read_csv(self.source_file.name)
        assert "language" in data.columns, (
            "Given source file has to contain a language column")
        country_codes = data["lanugages"]

        uniqe_elems = set(country_codes)
        self.oneHot = OneHotEncoder(sparse=False)

        # create the embeding scheme by fitting
        self.oneHot.fit([[x] for x in uniqe_elems])

    def _get_values(self, inputs):
        # create the encodings by applying transformation

        conv_inputs = [[value] for value in inputs[0]]
        return self.oneHot.transform(conv_inputs)
