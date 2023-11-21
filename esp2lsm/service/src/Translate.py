

from .Utils import Utils
import cv2

class Translate():
    def __init__(self):
        self.__vocab = Utils.createVocabulary()
        self.__path = '../raw/'
        self.__messageCount = 0

    def extractFrames(self, file_name):
        vidcap = cv2.VideoCapture(self.__path + file_name)
        success,image = vidcap.read()
        frames = []
        while success:
            frames.append(image) 
            success,image = vidcap.read()

        return frames
    
    def writeVideo(self, frames):
        self.__messageCount += 1
        dir_path = '/home/lara/Desktop/dactilologiaLSM_microservices/videos/'
        frameSize = (640, 480)
        out = cv2.VideoWriter(dir_path+'message{}.mp4'.format(self.__messageCount),cv2.VideoWriter_fourcc(*'MP4V'), 10, frameSize)
        for frame in frames:
            out.write(frame)
        out.release()

    def finish(self):
        #Borrar archivos del directorio videos
        pass
    
    def createVideo(self, message):
        words = self.searchWords(message)
        videoFrames = []
        for word in words:
            if isinstance(word, str):
                videoFrames.extend(self.extractFrames(word))

            else:
                for letter in word:
                    videoFrames.extend(self.extractFrames(letter))

        # Transform frames into video
        self.writeVideo(videoFrames)
        return 'message{}.mp4'.format(self.__messageCount)



    def searchWords(self, message):
        words = []
        for word in message:
            if self.isWordInVocab(word):
                words.append(self.__vocab[word])
            else:
                words.append(self.createSpellignVideo(word))

        return words

    def createSpellignVideo(self, word):
        spelling = []
        for letter in word:
            if self.isWordInVocab(letter):
                spelling.appned(self.__vocab[letter])

        return spelling

    def isWordInVocab(self, word):
        try:
            self.__vocab[word]
            return True
        except:
            return False