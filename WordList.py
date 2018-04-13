'''
Created on Mar 21, 2018

@author: jfernando
'''
from Word import Word

class WordList(object):

    def __init__(self):
        self.words = []
                    
    def add(self, contents):
        for v in contents:
            exists = False
            for r in self.words:
                if v.chars == r.chars:
                    exists = True
                    r.use(v.likes)
            if exists == False:
                self.words.append(v) 
        
    def sort(self):
        maxi = 0
        for x in range(1, len(self.words)):
            if self.words[x].ratio > self.words[max].ratio:
                maxi = x
        temp = self.words[0]
                    
    def print(self):
        for w in self.words:
            Word.print(w)