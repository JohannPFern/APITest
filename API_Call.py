'''
Created on Feb 28, 2018

@author: jfernando
'''
import requests
from WordList import WordList
from Word import Word
from Message import Message

#my groups
#data = requests.get("https://api.groupme.com/v3/groups?token=9d32f790f3d50135dba70bdb97628461")

#messages from Test
response = requests.get("https://api.groupme.com/v3/groups/38383709/messages?token=9d32f790f3d50135dba70bdb97628461")
#200 if response functions
#print(response)

#Gets all messages from chat
work = response.text
work = work[str.find(work,'\"messages\":')+12:len(work)-23]

#Make list of messages
messages = []
remaining = True
while (remaining == True):
    temp = work[:str.find(work,'},')+2]
    if "\"sender_id\":\"system\"" not in temp:
        messages.append(Message(temp))
    work = work[str.find(work,'},')+2:]
    if "}," not in work:
        remaining = False
if "sender_id: \"system\"" not in work:
    messages.append(Message(work))
words = WordList()
words.add(messages[1].contents)
WordList.print(words)