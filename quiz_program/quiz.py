""" A quiz is a selection of numbered questions"""

import question

class Quiz:
    'Base class for all types of quiz'

    def __init__(self, questioncount):
        self.quizsheet = []
        self.questioncount = questioncount
        for i in range(questioncount):
            newquestion = question.Question(i, 'abc' + str(i), ['Tokyo', 'Sydney', 'Moscow', 'Amsterdam'], 2)
            self.quizsheet.append(newquestion)

    def getQuestionByNumber(self, j):
        "Returns the question text"
        return self.quizsheet[j].getQuestionText()

    def getAnswerByNumber(self, k):
        "Returns the question text"
        return self.quizsheet[k].getAnswerText()
 
def main():
    print('generating test quiz')
    test_quiz = Quiz(6)

    print('question 2: ', test_quiz.getQuestionByNumber(2))
    print('answer: ', test_quiz.getAnswerByNumber(2))

if __name__ == "__main__":
    main()
