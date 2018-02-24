"""Interacts with the user, ask them questions, 
receive their answers, marks the answers, keeps the score and gives them 
their results at the end"""

from library.quizsheet import Quizsheet
from library.contestant import Contestant

class Game(object):
    'Returns a game object'
    def __init__(self):
        self.quiz = Quizsheet()
        self.contestant = Contestant(input('Enter your name\n> '))
        pass

    def play(self):
        for i in range(self.quiz.getNumberOfQuestions()):
            question = self.quiz.getQuestionByNumber(i).getQuestionText()
            print(question)
            print(self.quiz.getQuestionByNumber(i).getOptionsText())
            answer = int(input('> ')) - 1
            if answer == self.quiz.getQuestionByNumber(i).getAnswer():
                print('Correct.')
                self.contestant.updateScore(1)
            else:
                print('Sorry {0} that is wrong...\n The answer is... {1} '.format(self.contestant.getName(),self.quiz.getQuestionByNumber(i).getAnswerText()))

    def announceResults(self):
        print('Final score...')
        print(self.contestant.getScore())



