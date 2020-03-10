#Written by Pental
import re
import string
import sys
print ("Source by Pental")
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
result = findSentence('pslist.txt', "0x") #0x로 시작되는 모든 문장 result 에 저장
new_pslist_file = open('new_pslist_file.txt','w')
#new_pslist_file.txt 에 저장 / 한줄로 나옴
for sentence in result:
    i = len(sentence)
    new_pslist_file.writelines(sentence[0:i-1] + '\n') #줄 바꿈 소스
new_pslist_file.close()
# 각 프로세스를 리스트화 시키는 소스
with open('new_pslist_file.txt', 'r') as f:
    list_file = f.readlines()
list_file = [line.rstrip('\n') for line in list_file]
f = open('new_pslist_file.txt','r')
cnt = f.read().count("\n")+1
f.close()
n = 1

#Offset List
offset_list = []
for i in range(cnt-1):
    offset_list.append(list_file[i][0:10])
result = []
for i in offset_list:
    replace = i.replace(' ','')
    result.append(replace)
print(result)

#Name List
name_list = []
for i in range(cnt-1):
    name_list.append(list_file[i][10:30])
result = []
for i in name_list:
    replace = i.replace(' ','')
    result.append(replace)
print(result)

#Pid List
pid_list = []
for i in range(cnt-1):
    pid_list.append(list_file[i][34:39])
result = []
for i in pid_list:
    replace = i.replace(' ','')
    result.append(replace)
print(result)

#Ppid List
ppid_list = []
for i in range(cnt-1):
    ppid_list.append(list_file[i][42:46])
result = []
for i in ppid_list:
    replace = i.replace(' ','')
    result.append(replace)
print(result)

#Thds List
thds_list = []
for i in range(cnt-1):
    thds_list.append(list_file[i][49:53])
result = []
for i in thds_list:
    replace = i.replace(' ','')
    result.append(replace)
print(result)

#Hand List
hand_list = []
for i in range(cnt-1):
    hand_list.append(list_file[i][58:62])
result = []
for i in hand_list:
    replace = i.replace(' ','')
    result.append(replace)
print(result)

#Time List
time_list = []
for i in range(cnt-1):
    time_list.append(list_file[i][76:105])
result = []
for i in time_list:
    replace = i.replace(' ','')
    result.append(replace)
print(result)


pslist_result = []
#for i in range(cnt-1):
    #print (offset_list[i],name_list[i],pid_list[i],ppid_list[i],thds_list[i],hand_list[i],time_list[i])
