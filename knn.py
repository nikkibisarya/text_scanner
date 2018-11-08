import random
import math
import operator

from textscanner import text_file_vec_distance
from textscanner import text_file_to_vec
filePath = 'C:/Users/Boltak/Desktop/Research/addiction_transcripts'
fileName = ['transcripts_splits_data_new']

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_vec_representation(fileName, split, trainingSet=[] , testSet=[]): # check out tuples
    with open(''.join([filePath,fileName]), 'r') as file:
        mylist = [tuple(map(float, i.split(','))) for i in f]
        lines = file.readlines()
        dataset = list(lines)
        for x in range(len(dataset)): # check range start index
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split: # seed this
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
 
def get_feature_label(line):
        empathy = tuple[6]
    return empathy
 
def get_neighbors(trainingSet, testInstance, k):
    distances = {}
    for x in range(len(trainingSet)):
        dist = text_file_vec_distance(testInstance, trainingSet[x])
        distances[trainingSet[x]] = dist # takes into account feature when calculating distance
    distances.sort(key=operator.itemgetter(1))# make label into a tuple instead of putting into a vector
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors
 
def get_response(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1] 
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
 
def get_accuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
    
def main():
    # prepare data
    trainingSet=[]
    testSet=[]
    split = 0.67
    get_vec_representation('some.data', split, trainingSet, testSet)
    print ('Train set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))
    # generate predictions
    predictions=[]
    k = 3
    for x in range(len(testSet)):
        neighbors = get_neighbors(trainingSet, testSet[x], k)
        result = get_response(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = get_accuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')
    
main()