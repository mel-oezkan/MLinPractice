#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converts the entries from the dataset into useful features.

@author: meloezkan
"""

import numpy as np
import string
from code.feature_extraction.feature_extractor import FeatureExtractor


class DataFeatures(FeatureExtractor):

    def __init__(self, input_column, value_representation):
        # names the input column the same way was in the data
        super().__init__([input_column], input_column)
        # specify if the number representation is float or int
        assert value_representation in ['float', 'int'], (
            "The value representation only takes the \
            inputs: [float, int]")

        self.representation = value_representation
        self.numeric_error = "Input is not numeric\
            either format was set wrong or data is not \
            compatible with numeric values"

    # takes the inputs, checks them, converts them into
    # ints and appends them to the features
    def _get_values(self, inputs):
        if self.representation == "int":
            converter = self.convert_int
        else:
            converter = self.convert_float

        converted_features = []
        for line in inputs[0]:
            converted_features.append(converter(line))

        return converted_features

    def convert_int(self, input: string) -> int:
        assert input.isnumeric(), self.numeric_error

        return int(input)

    def convert_float(self, input: string) -> float:
        # split the input such that we get a number before
        # and after the decimal point to check and return
        split_values = input.split('.')
        numeric_boolean = [value.isnumeric() for value in split_values]

        assert all(numeric_boolean), self.numeric_error
        return float(input)
