#Written by Pental
# 특정 프로세스 정보 추출
import re
import string
import sys

# Function
#Find Unique Word

def findSentence(fileName, findText):
    file = open(fileName, mode="r", encoding="utf8")
    result = []
    data = file.read()
    data = data.splitlines()
    for line in data:
        sentences = line.split(". ")
        for sentence in sentences:
            sentence = sentence.strip(".")
            if findText in sentence:
                result.append(sentence + ".")
    file.close()
    return result

#Delete Special Text
def cleanText(readData):
    text = re.sub('[(),:]','',readData)
    return text

#---------------Find Image--------------
#Find Unique Word (Win)
print ("Source by Pental / Please input Accurate Process Name!!")
unique = input("Find Unique Process Information : ")

result = findSentence('pslist.txt',unique)

for sentence in result:
    result = sentence

name = result[10:30]
pid = result[35:39]
ppid = result[42:46]
thds = result[49:53]
hand = result[58:62]
time = result[76:105]
print ('Process Name : ' + name)
print ('Pid : ' + pid)
print ('Ppid : ' + ppid)
print ('Threads : ' + thds)
print ('Handle : ' + hand)
print ('Time : ' + time)