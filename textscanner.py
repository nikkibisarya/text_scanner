from asyncore import write

def text_file_vec_distance(v1, v2):
    dist = 0
    if len(v1) != len(v2):
        raise ValueError('Not matching dimensions')

    for i in range(len(v1)):
        dist += (v1[i] - v2[i]) ** 2
        
    dist = dist/len(v1)    
    return dist


def text_file_to_vec(filePath, filename, allWords):
    wordFreqVec = {}
    for word in allWords:
        wordFreqVec[word] = 0
    
    with open(''.join([filePath,filename]), 'r') as file:
        for line in file:
            for word in line.split():
                wordFreqVec[word] += 1
        
    retVec = []    
    for word in wordFreqVec:
        retVec.append(wordFreqVec[word])
    
    return retVec

# allWords = []
# for textFileName in textFileNames:
#     with open(''.join([filePath,textFileName]), 'r') as file:
#         for line in file:
#             for word in line.split():
#                 if not word in allWords:
#                     allWords.append(word)
# 
# textFile = open(''.join([filePath,'allWords.txt']), 'w')
# for word in allWords:
#     textFile.write(''.join([word,'\n']))
#     
# textFile.close()
#     
# wordFreqVecs = []
# 
# for textFileName in textFileNames:
#     
#     textFile2 = open(''.join([filePath,'wordFreqVec.txt', textFileName]),'w')
#     for word in wordFreqVec:
#         textFile2.write(''.join([str(wordFreqVec[word]),'\n']))
#     vectDist = tuple(open(''.join([filePath,'wordFreqVec.txt', textFileName]), 'r'))
#     textFile2.close()
#     
#     distance(vectDist, vectDist2)
