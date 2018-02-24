""" A question has an ID, some question text, some options, and a correct answer """

class Question:
    'Common base class for all questions'

    def __init__(self, qid, question_text, options, answer_index):
        self.qid = qid
        self.question_text = question_text
        self.options = options
        self.answer_index = answer_index

    def getQuestionText(self):
        "Returns the question text"
        return self.question_text

    def getAnswer(self):
        "Returns the index of the answer as an integer"
        return self.answer_index

    def getAnswerText(self):
        answer_text = self.options[self.answer_index]
        return answer_text

    def getOptionsText(self):
        text = ''
        for i in range(len(self.options)):
            text += '{0}) {1} \n'.format(str(i+1), self.options[i])

        return text

    def getId(self):
        "Returns the ID of the question"
        return self.qid