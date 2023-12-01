from .Utils import Utils
import cv2
import os
import time
class Translate():
    def __init__(self):
        self.__vocab = Utils.createVocabulary()
        self.__path = '../raw/'
        self.__messageCount = 0
        self.__pubicVideoPath = '/home/lara/Desktop/LSM/microservices/deafUI_web/videos_robot/'


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
        # dir_path = '/home/lara/Desktop/dactilologiaLSM_microservices/deafUI/videos_robot/'
        frameSize = (640, 480)
        out = cv2.VideoWriter(self.__pubicVideoPath+'message{}_tmp.mp4'.format(self.__messageCount),cv2.VideoWriter_fourcc(*'mp4v'), 20.0, frameSize)
        for frame in frames:
            # x = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            x = cv2.resize(frame, frameSize)
            out.write(x)
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
        videoName = self.__pubicVideoPath + 'message{}.mp4'.format(self.__messageCount)
        tmp = self.__pubicVideoPath + 'message{}_tmp.mp4'.format(self.__messageCount)
        os.system("ffmpeg -i {} -vcodec libx264 -f mp4 {}".format(tmp, videoName))
        # os.remove(tmp)
        return 'message{}.mp4'.format(self.__messageCount)



    def searchWords(self, message):
        words = []
        for word in message.split():
            if self.isWordInVocab(word):
                words.append(self.__vocab[word])
            else:
                words.append(self.createSpellignVideo(word))

        return words

    def createSpellignVideo(self, word):
        spelling = []
        for letter in word:
            if self.isWordInVocab(letter):
                spelling.append(self.__vocab[letter])

        return spelling

    def isWordInVocab(self, word):
        try:
            self.__vocab[word]
            return True
        except:
            return False