"Reads in questions from a source and turns into a list"

import csv

class QuestionImporter:
    'Base class for all types of quiz'

    def __init__(self):
        with open('questions.csv', "rt", encoding="ascii") as f:
            reader = csv.reader(f)
            self.questions = list(reader)

    def getQuestionData(self):
        return self.questions
