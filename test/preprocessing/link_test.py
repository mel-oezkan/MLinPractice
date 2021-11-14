#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: meloezkan
"""

import unittest
from numpy.testing._private.utils import assert_equal
import pandas as pd

from code.preprocessing.link_remover import LinkRemover

class LinkTest(unittest.TestCase):
    
    def setUp(self):
        self.INPUT_COLUMN = "input"
        self.OUTPUT_COLUMN = "output"

        self.df = pd.DataFrame()
        self.df[self.INPUT_COLUMN] = [
            "This tweet has a link in it https://t.co/VXUy6wPcTv",
            "This tweet also has a link in it https://t.co/ABAmiX2000",
        ]

        self.expected_output = [
            "This tweet has a link in it LinkContent",
            "This tweet also has a link in it LinkContent",
        ]

        self.stopword_remover = LinkRemover(self.INPUT_COLUMN, self.OUTPUT_COLUMN)
        self.preproecessing_output = self.stopword_remover.fit_transform(self.df[self.INPUT_COLUMN])

    def test_input_column(self):
        self.assertListEqual([self.INPUT_COLUMN], self.stopword_remover._input_columns)

    def test_output_column(self):
        self.assertListEqual([self.OUTPUT_COLUMN], self.stopword_remover._output_column)

    def test_preprocessing(self):
        """Test if the ouput look as expected"""
        
        # zip for easier iteration
        zipped_outputs = zip(
            self.expected_output,
            self.preproecessing_output
        )

        for expected, output in zipped_outputs:
            self.assertEqual(expected, output)
