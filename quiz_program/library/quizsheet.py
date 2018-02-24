""" A quizsheet is a selection of numbered questions 
that can be returned using their index """

from library.question import Question
from library.importer import Importer

class Quizsheet(object):
    'Returns a quizsheet object'

    def __init__(self):
        self.questionlist = [] 
        imported = Importer()
        self.questioncount = imported.getNumberImported()
        for i in range(imported.getNumberImported()):
            newquestion = Question(i, imported.getCell(i,0), [ imported.getCell(i,1), imported.getCell(i,2), imported.getCell(i,3), imported.getCell(i,4)], int(imported.getCell(i,5)))
            self.questionlist.append(newquestion)

    def getQuestionByNumber(self, j):
        "Returns a question object when supplied a valid index"
        return self.questionlist[j]

    def getNumberOfQuestions(self):
        "Returns the number of questions in the quiz"
        return self.questioncount
