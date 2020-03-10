#Written by Pental
#Imageinfo 실행시 나오는 결과중 중요한것 추출
print ("Source by Pental / Extract Important Imageinfo Information \n")
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
result = findSentence("image.txt", "Win")

for sentence in result:
    extact_sentece = sentence

if __name__ == "__main__":
    oriText = extact_sentece
#    print('Del Special word : ', cleanText(oriText))
    del_speical_word_image = cleanText(oriText)

#Del SpaceBar
replace_space_bar_image = del_speical_word_image.replace(" ","")

image_information = replace_space_bar_image[17:28]
print ('Image Profile :',image_information)

#--------------------------FileAddressSpace---------------------
fileaddress = findSentence("image.txt", "FileAddressSpace")
#Del Unique Word - File Space
for sentence in fileaddress:
    file_space = sentence

if __name__ == "__main__":
    oriText = file_space
    del_speical_word_file_space = cleanText(oriText)

#Del Space Bar - File Space
replace_space_bar_file_space = del_speical_word_file_space.replace(" ","")
i = len(replace_space_bar_file_space)
file_space = replace_space_bar_file_space[24:i-1]
print ('Image File Address :',file_space)

#------------Image date and time--------------
imagedataandtime = findSentence("image.txt", "Image date and time")
#Del Unique Word - Image date and time
for sentence in imagedataandtime:
    image_data_and_time = sentence

if __name__ == "__main__":
    oriText = image_data_and_time
    del_speical_word_image_data_and_time = cleanText(oriText)

#Del Space Bar - Image date and time
replace_space_bar_image_data_and_time = del_speical_word_image_data_and_time.replace(" ","",12)
i = len(replace_space_bar_image_data_and_time)
image_data_and_time = replace_space_bar_image_data_and_time[20:i-1]
print ('Image Data And Time :',image_data_and_time)