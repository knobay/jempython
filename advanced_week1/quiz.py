class Question:
   'Common base class for all questions'

   def __init__(self, question_number, question, answer):
      self.question_number = question_number
      self.question = question
      self.answer = answer



   def askQuestion(self):
     print(self.question, "?")

   def giveAnswer(self):
     print(self.answer)

   def announceNumber(self):
     print(self.question_number)    

def startquiz():
    questions = []
    questions.append(Question(1, "What is the captial of France", "Paris"))
    questions.append(Question(2, "What is the captial of Germany", "Berlin"))
    questions.append(Question(3, "Who wrote Animal Farm", "George Orwell"))
    questions.append(Question(4, "In what yaer did World War 2 start in Europe", "1945"))

    for question in questions:
        question = questions.pop()
        question.announceNumber()
        user_answer = input(question.askQuestion())
        print('the answer is...')
        question.giveAnswer()
        if user_answer==question.answer:
            print('Well done!')

def main():
    startquiz()

main()