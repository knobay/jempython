"""Interacts with the user, ask them questions, 
receive their answers, marks the answers, keeps the score and gives them 
their results at the end"""

from library.quizsheet import Quizsheet
from library.contestant import Contestant


class Game(object):
    'Returns a game object'

    def __init__(self, name, duration):
        self.quiz = Quizsheet()
        self.contestant = Contestant(name)
        self.totalquestions = int(duration)
        pass

    def play(self):
        for i in range(self.totalquestions):
            thisquestion = self.quiz.getQuestionByNumber(i)

            print(chr(27) + "[2J")  # clear screen

            print(thisquestion.getQuestionText())
            print(thisquestion.getOptionsText())

            'Get the users answer \
            If the user does not want to quit, \
            cast their answer as an integer and correct for zero based index.'

            answer = input('\n> ')
            if answer.upper() != 'Q':
                try:
                    answer = int(answer) - 1
                except:
                    answer = None

            print(chr(27) + "[2J")  # clear screen

            if answer == thisquestion.getAnswer():
                print('Correct.')          
                self.contestant.updateScore(1)
                input('\n>')
            elif answer:
                print('Sorry {0} that is incorrect. The answer is {1}. '.format(self.contestant.getName(), thisquestion.getAnswerText()))
                input('\n>')
            else:
                print('Invalid input. The answer is {0}. '.format(thisquestion.getAnswerText()))
                input('\n>')

        print(chr(27) + "[2J")  # clear screen

        print('{0}, you scored {1} out of {2}\n'.format(self.contestant.getName(), self.contestant.getScore(), self.totalquestions))
        again = input('Play again? (Y) \n\nAny other key to quit\n\n> ')
        if again.upper() == 'Y':
            newgame = Game(self.contestant.getName(), self.totalquestions)
            newgame.play()
