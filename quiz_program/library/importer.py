"Reads in questions from an external source"

import csv
import random

class Importer(object):
    'Returns QuestionImporter object'

    def __init__(self):
        with open('data/questions.csv', "rt", encoding="ascii") as f:
            reader = csv.reader(f)
            self.questions = list(reader)

    def getNumberImported(self):
        return len(self.questions)

    def getCell(self, i, j):
        'returns data point from import by cell reference'
        return self.questions[i][j]

    def getQuestionData(self):
        return self.questions
