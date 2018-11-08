import pandas as pd
import numpy as np

FILE_PATH = 'C:\\Users\\Owner\\Desktop\\meta.data.4.03.13.csv'

df = pd.read_csv(FILE_PATH, encoding='latin1')

valid_symps = df['Symptoms'].dropna()

all_symp_colls = valid_symps.tolist()


rows = []

all_symps = []
for symp_coll_str in all_symp_colls:
    symp_strs = [symp_str.strip() for symp_str in symp_coll_str.split(';')]
    rows.append(symp_strs)
    all_symps.extend(symp_strs)

all_symps = list(set(all_symps))

print(all_symps)

symp_vecs = []
for row in rows:
    zero_vec = [0] * len(all_symps)
    for word in row:
        set_index = all_symps.index(word)
        zero_vec[set_index] = 1

    symp_vecs.append(zero_vec)

symp_vecs = np.array(symp_vecs)

print(df.columns)

file_to_symp_vec = dict(zip(df['dorp_hierarchy'].tolist(), symp_vecs))

def remove_invalid(s):
    s = str(s)
    s = s.lower()
    initial = 0
    i = 0

    while i < len(s):
        c = s[i]
        if c == '(' or c == '[':
            initial = i
        if c == ')' or c == ']':
            tmp = s[:initial]
            tmp.extend(s[i + 1:])
            s = tmp
            i = initial
    return s

TRANSCRIPT_FILE_PATH = 'C:\\Users\\Owner\\Desktop\\General_psychtx_corpus_phase1.1.csv'

print('Loading new')
tdf = pd.read_csv(TRANSCRIPT_FILE_PATH, encoding='latin1')

print(len(tdf))
print('Mapping')
good_lines = [remove_invalid(line) for line in tdf['dialogue'].tolist()]
print('Done mapping')
print(good_lines[:5])

#print(symp_vecs.shape)
#TfidVectorizer()
#MultiLayerBinarizer
#fit_transform
