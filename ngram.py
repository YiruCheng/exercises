# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 23:48:55 2018

@author: Yi-Ru
"""

import nltk

"""
*Word n-gram function*

Please, implement the word n-gram function.
Consider the text and the number of items per n-gram as input parameters to the function. 
Print results for n=1, n=2 and n=3 to the console.
"""

class Ngram(object):
    def __init__(self, text):
        self.text = text
        self.sentences = [s for s in nltk.tokenize.sent_tokenize(text)]
        self.tokens = {}
        for i in range(len(self.sentences)):
            s = self.sentences[i]
            self.tokens[i] = ['<start>']
            self.tokens[i].extend([t for t in nltk.tokenize.word_tokenize(s)])
        
    def generate(self, num):
        result = {}
        for key, tokens in self.tokens.items():
            grams = []
            for i in range(len(tokens)-num+1):
                gram = []
                for j in range(num):
                    gram.append(tokens[i+j])
                grams.append(gram)
            result[key] = grams
        return result
    
    
if __name__ == '__main__':
    text = 'I love pizza. I love cola.'
    obj = Ngram(text)
    for i in range(1, 4):
        print('n='+str(i))
        results = obj.generate(i)
        for k, tokens in results.items():
            print(str(k+1)+' sentence:')
            print(tokens)
