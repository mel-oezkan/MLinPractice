#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: meloezkan
"""

import unittest
import pandas as pd

from code.preprocessing.stopword_remover import StopWords

class StopwordTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.OUTPUT_COLUMN = "output"

        self.stopword_remover = StopWords(self.INPUT_COLUMN)
    
    def test_removal_single(self):
        input_tokens = "[\
            'This', 'sentence', 'has', 'many',\
            'stopwords', 'and', 'this', 'can',\
            'be', 'a', 'small', 'problem'\
        ]"

        expected_output = None

        