""" A question has an ID, some question text, some options, and a correct answer """

class Question(object):
    'Returns a question object if supplied all the \
    required attributes as parameters: id (integer), questions text, \
    list of options and an answer index (integer referring to the correct answer from the options)'

    def __init__(self, qid, questiontext, options, answer):
        self.qid = qid
        self.questiontext = questiontext
        self.options = options
        self.answer = answer

    def getQuestionText(self):
        "Returns the question text"
        return self.questiontext

    def getAnswer(self):
        "Returns the index of the answer as an integer"
        return self.answer

    def getAnswerText(self):
        answertext = self.options[self.answer]
        return answertext

    def getOptionsText(self):
        text = ''
        for i in range(len(self.options)):
            text += '{0}) {1} \n'.format(str(i+1), self.options[i])
        return text

    def getId(self):
        "Returns the ID of the question"
        return self.qid