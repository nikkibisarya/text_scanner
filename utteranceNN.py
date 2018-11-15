import numpy as np
import re
filePath = r'C:\Users\Boltak\Desktop\2012-10-20-coding_data-all.txt'
word2VecPath = r'C:\Python\text_scanner\vec.txt'

def normalize_code(code):
#    print(code,spk)

    code = re.sub(r"(.*)([+-]).*", r"\1\2", code).upper()
    if code in ["FA","GI","RES","QUC","QUO","REC"]:
        pass
    elif code in ["ADW","CO","DI","RCW","WA"]:
        code = "NA"
    else:
        code = "COU"

    return code

#make a dictionary of each 
def make_dictionary(open_path):
    transcriptToUtterances = {}
    with open(open_path, 'r') as file:
        for line in file:
            values = line.split('\t')
            if len(values) == 10:
                if values[6] == 'T':
                    result = values[-1]
                    label = values[5]
                    label_code = normalize_code(label)
                    
                    add_pair = [result, label_code]
                    key = values[0]
                    
                    if key in transcriptToUtterances:
                        transcriptToUtterances[key].append(add_pair)
                    else:
                        transcriptToUtterances[key] = [add_pair] 
                else:
                    continue
            else:
                continue
            
    return transcriptToUtterances
            
def processWordVectors():
    with open(word2VecPath, 'r') as file:
        word2vecDict = {}
        isWord = False
        word = ''
        for line in file:
            for value in line.split():
                try:
                    fVal = float(value)
                    
                    if word in word2vecDict:
                        word2vecDict[word].append(float(value))
                    else:
                        word2vecDict[word] = [float(value)]
                except Exception:
                    word = str(value)
                
    return word2vecDict
            
def word2vec(transcriptToUtterances):
    word2vecDict = processWordVectors()
    file2AvgVecPerUtterance = {}
    
    for key in transcriptToUtterances:
        for utterance, label in transcriptToUtterances[key]:
            listOfWordVecs = []
            for word in utterance.split(' '):
                if word in word2vecDict:
                    listOfWordVecs.append(word2vecDict[word])
            if len(listOfWordVecs) == 0:
                continue
            listOfWordVecs = np.array(listOfWordVecs)
            
            avgVec = np.mean(listOfWordVecs, axis=0)
            
            add_pair = [avgVec, label]
            
            if key in file2AvgVecPerUtterance:
                file2AvgVecPerUtterance[key].append(add_pair)
            else:
                file2AvgVecPerUtterance[key] = [add_pair]
                
    return file2AvgVecPerUtterance


utters = make_dictionary(filePath)
print('done!')
trans_to_utters = word2vec(utters)  
print('i love nikki!')
                 