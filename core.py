#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:18:08 2020

@author: agastya
"""
from summarizer import Summarizer
from transformers import *


class Summary:
    def __init__(self, num_sentences=None, ratio=0.3, model=None, tokeniser=None):
        '''
        

        Parameters
        ----------
        model : string, optional
            Custom model configuration. The default is None.
        tokeniser : string, optional
            Custom tokeniser configuration. The default is None.

        Returns
        -------
        None.

        '''
        if model is not None or num_sentences is not None:
            custom_config = AutoConfig.from_pretrained(model)
            custom_config.output_hidden_states=True
            custom_tokenizer = AutoTokenizer.from_pretrained(mo)
            custom_model = AutoModel.from_pretrained(model, config=custom_config)
    def model(self):
        '''
        

        Returns
        -------
        model : summariser object

        '''
        if model is not None or num_sentences is not None:
            model = Summarizer()
        else:
            model = Summarizer(custom_model=custom_model, custom_tokenizer=custom_tokenizer)
        
        return model
    def summarize(self, text, num_sentences=None, ratio=0.3):
        '''
        

        Parameters
        ----------
        text : string
            text to be summarised.
        num_sentences : int, optional
            Number of sentences the text should be condensed into. The default is None.
        ratio : float, optional
            Speicifies how much of the original text must the summary represent lengthwise. The default is 0.3.

        Returns
        -------
        result : string
            Summarised text.

        '''
        model = self.model()
        summary = model(text, num_sentences, ratio)
        result = ''.join(summary)
        
        return result
            