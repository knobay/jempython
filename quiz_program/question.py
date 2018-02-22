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

    def getId(self):
        "Returns the Id of the question"
        return self.qid

def main():
    print('generating test question')
    test_question = Question(123, 'What is the capital of Russia?', ['Tokyo', 'Sydney', 'Moscow', 'Amsterdam'], 2)
    print(test_question.getQuestionText(), '\nOptions are... ')

    for item in test_question.options:
        print(item + '\n')

    print('correct answer is ', test_question.getAnswerText())

if __name__ == "__main__":
    main()
