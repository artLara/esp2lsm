import os
# files = [f for f in os.listdir('../raw/') if os.path.isdir(f)]

class Utils():

    def createVocabulary():
        vocab = {}
        files = os.listdir('../raw/')
        for file in files:
            word = ''.join(file.replace('.mp4', '_').split('_')[1::])
            vocab[word] = file
            # print(word)
        return vocab
