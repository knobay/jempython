"""A contestant has a name and a score"""

class Contestant(object):

    score = 0

    'Returns a Contestant object with a score of zero when supplied a contestant name as string'
    def __init__(self, name):
        self.name = name

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def updateScore(self,update):
        self.score += update
        return

