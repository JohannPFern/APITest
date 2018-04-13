'''
Created on Mar 21, 2018

@author: jfernando
'''
from Word import Word

class Message(object):
    text = ""
    contents = []
    likes = 0

    def __init__(self, s):
        self.text = s[str.find(s,"\"text\":")+8:str.find(s,",user_id:")-23].lower()
        temp = s[str.find(s,"by\":")+4:str.find(s,",\"group")]
        if "," in temp:
            x = temp.split(",")
            self.likes = len(x)
        elif "\"" in temp:
            self.likes = 1
        else:
            self.likes = 0
        v = self.text.split(" ") 
        for g in v:
            self.contents.append(Word(g,self.likes))
        
    def getText(self):
        return self.text
    
    def print(self):
        print(Message.getText(self)+str(self.likes))