#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remove Links contained in the tweet

@author: meloezkan
"""

import re

from code.preprocessing.preprocessor import Preprocessor

class LinkRemover(Preprocessor):
    """Remove stop words from the tokenized words."""
    
    def __init__(self, input_column, output_column):
        """Initialize the Tokenizer with the given input and output column."""
        super().__init__([input_column], output_column)
    
    def _set_variables(self, inputs):
        self.pattern = re.compile('https://t.co/([a-z]|[A-Z]|[0-9])*')

    def _get_values(self, inputs):
        """Search for the pattern and replace them"""

        print('    Running Link Remover')

        without_links = []
        for tweet in inputs[0]:
            pattern_match = self.pattern.findall(tweet)

            # checks if link in tweet        
            if pattern_match:
                
                # since pattern match can be multiple objects iterate over them
                for match in pattern_match:
                    tweet.reaplace(match.group(), "LinkContent")

            without_links.append(tweet)
            
        return without_links