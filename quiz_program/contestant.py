""" A contestant has a name and a score  """

class Contestant():

    score = 0

    'Base class for all types of contestant'
    def __init__(self, name):
        self.name = name

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def updateScore(self,update):
        self.score += update
        return

