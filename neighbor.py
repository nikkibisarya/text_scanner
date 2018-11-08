import math
from _sqlite3 import Row

def get_vec_representation(text):
    pass


def get_dist(v0, v1):
    pass


def get_label_feature(text):
    return (some_feature, some_label)


def k_nn(target, samples, k):
    min_dists = []
    for i in range(k):
        min_dists.append((0., -1))
        
    for sample in samples:
        feature = sample[0]
        label = sample[1]
        dist = get_dist(feature, target)
        for i in range(len(min_dists)):
            min_dist = min_dists[i][0]
            if min_dist > dist:
                min_dists[i] = (dist, label)
                
    sum = 0.
    for min_label in [min_dist[1] for min_dist in min_dists]:
        sum += float(min_label)
    avg /= float(k)
    nearest_label = math.ceil(avg)
    
    return nearest_label
    
        
def main(target):
    # Load all your data.
    
    DELIMITER = '-'
    TEXT_FILENAME = 'path here'
    with open(TEXT_FILENAME, 'r') as f:
        all_text = f.read().replace('\n', '')
        
    texts = all_text.split(DELIMITER)
    all_data = []
    for text in texts:
        all_data.append(get_label_feature(text))
        
    all_data = [(get_vec_representation(all_data[0]), all_data[1]) for data in all_data]
    
    output_label = k_nn(target, all_data)
    
    return output_label









import csv

class TherapySession:
    filePath = 'C:/Users/Boltak/Desktop/Research/addiction_transcripts'
    fileName = ['transcripts_splits_data_new']
    TEXT_FILE_LOC = 'path to research folder'
    all_words = []
    
    def __init__(self, data):
        self.empathy = data["empathy"]
        self.text_file = data["session"]
        /
    
    def enc_freq(self):
        with open(TherapySession.TEXT_FILE_LOC + self.text_file + '.txt', 'r') as f:
            text = f.read().replace('\n', '')
            session_words = text.split(' ')
        #get all words, and then make feature vectors    
        self.freq_vec = [0] * len(TherapySession.all_words)
        for session_word in session_words:
            try:
                all_words_index = TherapySession.all_words.index(session_word)
            except Exception:
                all_words_index = -1
            
            if all_words_index == -1:
                TherapySession.all_words.append(session_word)
                self.freq_vec.append(1)
            else:
                self.freq_vec[all_words_index] += 1
                
    
    def get_enc_freq_vec(self):
        if len(self.freq_vec) != len(TherapySession.all_words):
            diff = len(TherapySession.all_words) - len(self.freq_vec)
            self.freq_vec.extend([0] * diff)
        return self.freq_vec
        
        

with open('overall_file.txt', 'r') as f:
    csvreader = csv.reader(f, delimiter=',')
    header = csvreader[0]    
    
    sessions = []
    for row in csvreader[1:]:
        header_vals = zip(header, row)
        row_dict = {}
        for header_val in header_vals:
            row_dict[header_val[0]] = header_val[1]
        session = TherapySession(row_dict)
        session.enc_freq()    
        sessions.append(session)
        
def get_neighbors(sessions, testInstance, k):
    distances = []
    for session in sessions:
        dist = text_file_vec_distance(testInstance, session.get_enc_freq_vec())
        distances.append((session, dist))# takes into account feature when calculating distance
    distances.sort(key=lambda x: x[1]])# make label into a tuple instead of putting into a vector
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0].empathy)
    return neighbors
    
    
    
        