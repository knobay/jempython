"""Interacts with the user, ask them questions, 
receive their answers, mark them, keep the score and give them 
their results at the end of the exam"""


import quiz
import contestant

class QuizMaster():
    'Base class for all types of QuizMaster'
    def __init__(self):
        self.quiz = quiz.Quiz()
        self.contestant = contestant.Contestant(input('Enter your name\n> '))
        pass

    def ask(self):
        for i in range(self.quiz.getNumberOfQuestions()):
            question = self.quiz.getQuestionByNumber(i).getQuestionText()
            print(question)
            print(self.quiz.getQuestionByNumber(i).getOptionsText())
            answer = int(input('> ')) - 1
            if answer == self.quiz.getQuestionByNumber(i).answer_index:
                print('Correct.')
                self.contestant.updateScore(1)
            else:
                print('Sorry {0} that is wrong...\n The answer is... {1} '.format(self.contestant.getName(),self.quiz.getQuestionByNumber(i).getAnswerText()))

    def announceResults(self):
        print('Final score...')
        print(self.contestant.getScore())



