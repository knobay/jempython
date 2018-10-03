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
            question = self.quiz.getQuestionByNumber(i).getQuestionText()
            
            print(chr(27) + "[2J") # clear screen
            
            print(question)
            print(self.quiz.getQuestionByNumber(i).getOptionsText())
 
            answer = input('\n> ')
            if answer.upper() != 'Q':
                try:
                    answer = int(answer) - 1
                except:
                    answer = 5
                
            print(chr(27) + "[2J") # clear screen
           
            if answer == self.quiz.getQuestionByNumber(i).getAnswer():
                print('Correct.')             
                self.contestant.updateScore(1)
                input('\n>')
            elif answer == 5: # exception raised above
                print('Invalid input. The answer is {0}. '.format(self.quiz.getQuestionByNumber(i).getAnswerText()))
                input('\n>')
            else:
                print('Sorry {0} that is wrong. The answer is {1}. '.format(self.contestant.getName(),self.quiz.getQuestionByNumber(i).getAnswerText()))
                input('\n>')

        print(chr(27) + "[2J") # clear screen
        
        
        print('{0}, you scored {1} out of {2}\n'.format(self.contestant.getName(),self.contestant.getScore(), self.totalquestions))
        again = input('Play again? (Y) \n\nAny other key to quit\n\n> ')
        if again.upper() == 'Y':
            newgame = Game(self.contestant.getName(), self.totalquestions)
            newgame.play()
            # self.contestant.updateScore(-self.contestant.getScore())
            # self.quiz = Quizsheet()
            # self.play()

