'''
Created on Mar 21, 2018

@author: jfernando
'''

class Word(object):

    def __init__(self, n, l):
        self.chars = n
        self.likes = l
        self.uses = 1
        self.ratio = 0
        
    def __iter__(self):
        return self.ratio
        
    def print(self):
        print(self.chars + " " + str(self.likes))
        
    def use(self, x):
        self.uses += 1
        self.likes = self.likes + x
        
    def ratio(self):
        if self.likes !=0:
            self.ratio = self.likes/self.uses
        else:
            self.ratio = 0
        return self.ratio