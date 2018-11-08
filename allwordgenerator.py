filePath = 'C:/Users/Boltak/Desktop/NIKKIJIMMY/nikki jimmy/clean_transcripts/'
fileName = 'transcript_splits_data_new.txt'
       
header = []
data = []
with open(''.join([filePath,fileName]), 'r') as file:
    for line in file:
        if len(header) == 0:
            header = line.strip().split(',')
        else:
            cur_line = line.strip().split(',')
            dictionary = dict(zip(header, cur_line))
            data.append(dictionary)
      
textFileContent = []
for cur_data in data:
    print(cur_data['session'])
    session_filepath = filePath + cur_data['session'] + '.txt'
    with open(session_filepath) as f:
        content = f.read()
    textFileContent.append(content)
    
with open('out.txt', 'r+') as r:
    for file in textFileContent:
        r.write(file)
    print(r.read())
    
#only use train files