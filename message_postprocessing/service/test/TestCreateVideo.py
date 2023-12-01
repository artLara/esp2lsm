import os
import sys
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../../../')

from src.Translate import Translate
class TestService():
    def __init__(self):
        self.__translate = Translate()
    
    def runTest(self):
        message = 'te vi venir'
        res = self.__translate.createVideo(message)
        print(res)

t = TestService()
t.runTest()