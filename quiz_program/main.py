""" The main program run at start up  """

import quiz_master

def main():
    myQuizMaster = quiz_master.QuizMaster()
    myQuizMaster.ask()
    print('Score...')
    myQuizMaster.announceResults()

if __name__ == "__main__":
    main()