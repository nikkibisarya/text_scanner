import numpy as np

transcriptfilePath ='C:/Users/Boltak/Desktop/NIKKIJIMMY/nikki jimmy/clean_transcripts/'
fileName = 'transcript_splits_data_new.txt'
otherfileName = 'vec.txt'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

header = []
skipCount = 0
keyWord = ""
wordvecs = []
word2vec = {}
word2avg = {}
sessiontoRating = {}
data = [] #list of dictionaries, includes header with each line
totalSum = 0
numWords = 0
empathyRating = 0
transcriptToRating = {}   
vecs2Avg = []
transcriptAvg = 0

with open(''.join([transcriptfilePath,fileName]), 'r') as file:
    for line in file:
        if len(header) == 0:
            header = line.strip().split(',')
        else:
            cur_line = line.strip().split(',')
            dictionary = dict(zip(header, cur_line))
            data.append(dictionary)
            
with open(''.join([transcriptfilePath,otherfileName]),'r') as f:
    for line in f:
        for word in line.strip().split():
            skipCount = skipCount + 1
            if skipCount <= 2:
                continue
            if skipCount == 3:
                keyWord = word
            else:
                if not is_number(word): #if it is a word
                    if wordvecs:
                        word2vec[keyWord] = wordvecs[:]
                        wordvecs[:] = []
                    keyWord = word
                else: #if it is a number
                    if is_number(word):
                        wordvecs.append(word) #list of numbers for each word
               
for cur_data in data:
    session_filepath = transcriptfilePath + cur_data['session'] + '.txt'
    with open(session_filepath,'r') as transcript:
        for line in transcript:
            for word in line.strip().split():
                #print(word)
                if word in word2vec: #I wonder why not all the keys exist in the dictionary if they are in the transcript?
                    vecs2Avg.append(word2vec[word])
                    
        npvecs2Avg = np.array(vecs2Avg).astype(np.float)
        transcriptAvg = np.mean(npvecs2Avg, axis=0)
        transcriptToRating[cur_data['session']] = transcriptAvg.tolist()
        vecs2Avg = []
    
f = open('transcripttoavgvector.txt', 'w')    
for key in transcriptToRating:
    value = transcriptToRating[key]
    strvalue = ', '.join(str(e) for e in value)
    f.write(' '.join((key, ": ", strvalue)))
    f.write('\n')
f.close()
    
