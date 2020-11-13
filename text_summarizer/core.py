# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:18:08 2020

@author: agastya
"""
from summarizer import Summarizer
from transformers import AutoConfig, AutoTokenizer


class Summary:
    def __init__(self, model=None, tokenizer=None):
        if model == None:
            self.model = Summarizer()
        else:
            custom_config = AutoConfig.from_pretrained(model)
            custom_config.output_hidden_states=True
            custom_tokenizer = AutoTokenizer.from_pretrained(tokenizer)
            self.model = Summarizer(custom_model=model, custom_tokenizer=custom_tokenizer)

    
    def summarizeAdvanced(self, text, num_sentences=None, ratio=None):
        """[summary]

        Args:
            text (string): Text body to summarize.
            num_sentences (int, optional): Number of sentences the summary must consist of. Defaults to None.
            ratio (float, optional): The ratio of length of summary text to the original text. Defaults to None.

        Returns:
            [type]: [description]
        """
        if num_sentences is None:
            summary = self.model(text)
            result = ''.join(summary)
        elif ratio is None and num_sentences is not None:
            summary =self. model(text, min_length=num_sentences)
            result = ''.join(summary)
        elif ratio is not None:
            summary = self.model(text, ratio=ratio)
            result = ''.join(summary)

        return result

    def summarize(self, text):
        summary = self.model("TESTING AWESOME AMAZING")
        summary = self.model(text)
        result = ''.join(summary)
        return result

