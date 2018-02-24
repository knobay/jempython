""" A quiz is a selection of numbered questions """

import question
import questionimporter

class Quiz:
    'Base class for all types of quiz'

    def __init__(self):
        self.quizsheet = [] 
        questionlist = questionimporter.QuestionImporter()
        qs = questionlist.getQuestionData()
        self.questioncount = len(qs)
        for i in range(self.questioncount):
            newquestion = question.Question(i, qs[i][0], [ qs[i][1], qs[i][2], qs[i][3], qs[i][4]], int(qs[i][5]))
            self.quizsheet.append(newquestion)

    def getQuestionByNumber(self, j):
        "Returns a question"
        return self.quizsheet[j]

    def getNumberOfQuestions(self):
        "Returns the number of questions in the quiz"
        return self.questioncount
