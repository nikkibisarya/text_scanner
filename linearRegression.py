from operator import itemgetter
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import statistics
import numpy as np
from cmath import sqrt
from scipy.stats import pearsonr
filePath = 'C:/Users/Boltak/Desktop/Research/NIKKIJIMMY/nikki jimmy/clean_transcripts/'
fileName = 'transcript_splits_data_new.txt'
transcriptFile = 'C:/Python/text_scanner/transcripttoavgvector.txt'

#SVM, MLP, LDA -- Classification
#Support Vector Regression
# what type of parameters they will need
#write a report comparing these and their results in terms of unweighted aerage recall for classification
#and pearson's correlation for regression

# get words from all the text filess
def get_all_words(textFileNames):
    all_words = {}
    count = 0
    for textFileName in textFileNames:
        with open(textFileName, 'r') as file:
            for line in file:
                for word in line.split():
                    if word not in all_words:
                        all_words[word] = 0
                        
def read_in_file(file):
    testSet = {}
    sessionName = ""
    numberVector = []
    sessionVec = []
    #read in file by line
    with open(file, 'r') as f:
        for line in f:
            line = line.replace(" ", "")
            #split by :
            lineVec = line.split(':')
            #first is session name
            sessionName = lineVec[0]
            #second is vector
            #split vector by ,
            numberVector = lineVec[1].split(',')
            #convert each of those to floats
            for num in numberVector:
                #push that into a vector
                sessionVec.append(float(num))
            #pair session name with vector in dictionary
            testSet[sessionName] = sessionVec[:]
            sessionVec[:] = []
    #return dictionary
    return testSet

def convertFiletoDict(file):
    d = {}
    for line in file:
        #print(line)
        lineContent = line.split(':')
        #print(lineContent)
        #raise ValueError()
        lineContent[0] =  lineContent[0].strip(' ')
        #print(lineContent[0])
        strVecContent = lineContent[1].split(',')
        
        float_vector = []
        for str in strVecContent:
            str.strip(' ')
            float_vector.append(float(str))
        d[lineContent[0]] = float_vector
    return d
        
def main(model):
    # prepare data
    allWords = {}
    trainingSet=[]
    testSet=[]
    truePos = 0
    trueNeg = 0
    falsePos = 0
    falseNeg = 0
    header = []
    data = []
    calculatedVectOfVectors = []
    sessionToNumVec = {}
    
    
    with open(transcriptFile, 'r') as readFile:
        sessionToNumVec = convertFiletoDict(readFile)
    with open(''.join([filePath,fileName]), 'r') as file:
        for line in file:
            if len(header) == 0:
                header = line.strip().split(',')
            else:
                cur_line = line.strip().split(',')
                dictionary = dict(zip(header, cur_line))
                data.append(dictionary)
                
    sessions = []
    textFileNames = []
    for cur_data in data:
        study_folder = cur_data['study']
        study_folder = study_folder.split('_')[0]
        
        session_filepath = filePath + cur_data['session'] + '.txt'
        textFileNames.append(session_filepath)
        
        test = cur_data['split.patient.70/30'] == 'test'
        #print(sessionToNumVec[cur_data['session']])
        sessions.append({
            'test': test,
            'session_filepath': session_filepath,
            'session_name': cur_data['session'],
            'words': sessionToNumVec[cur_data['session']],
            'empathy': float(cur_data['empathy'])
            })   
        
    allWords = get_all_words(textFileNames)
    transcript_to_vec = read_in_file(transcriptFile)
    test_set = [session for session in sessions if session['test']]
    training_set = [session for session in sessions if not session['test']]
    # Fill these out with data from training_set
    X = [] #word vectors?
    Y = [] #empathy ratings? y > 5 is 1, y < 5 is 0
    # Fill these out with data from test_set
    test_X = [] #word vectors?
    test_Y = [] #empathy ratings?
    
    for session in sessions:
        for set in test_set:
            test_X.append(set['words'])
            test_Y.append(set['empathy'])
        for set in training_set:
            #print(set['words'])
            X.append(set['words'])
            Y.append(set['empathy'])
    # Fit model to the data (call your .fit(X, Y) function)
    for empathy_rating in Y:
        if empathy_rating < 5:
            empathy_rating = 0
        else:
            empathy_rating = 1
    for empathy_rating in test_Y:
        if empathy_rating < 5:
            empathy_rating = 0
        else:
            empathy_rating = 1
            
    model.fit(np.array(X), np.array(Y))
    predictions_y = model.predict(np.array(test_X))
    print('Predictions: ', predictions_y)
    print("Mean Squared Error: ", mean_squared_error(test_Y, predictions_y))
    print('\nPearsons Correlation Coefficient: ' + str(pearsonr(test_Y, predictions_y)))
    #make it binary and commpute the measures I was computing before
    
main(LinearRegression())       