#Written by Pental
#Cmdscan 결과 추출
print ("Source by Pental / Extract CmdScan Result")
import re
import string

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
result = findSentence("cmdscan.txt", "Cmd")

for sentence in result:
    extact_sentece = sentence
    print (extact_sentece[:-1])
