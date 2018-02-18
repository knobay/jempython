"""Quiz questions, a list of questions along with their answers"""

q01 = {
    'qnum' : 'Question 1',
    'qtext' : 'What is the answer to life, the universe and everything? ',
    'answtype' : 'int',
    'qansw' : 42
}

q02 = {
    'qnum' : 'Question 2',
    'qtext' : 'How do I get from Tokyo to Hawaii? ',
    'answtype' : 'text',
    'qansw' : 'Swim' #, 'Fly']
}

qquestions = [q01, q02]

print('')

for i in range(0,len(qquestions)):
    print(qquestions[i]['qnum'])
    ans = input(qquestions[i]['qtext'])
    if qquestions[i]['answtype'] == 'int' and int(ans) == qquestions[i]['qansw']:
        print('You just proved your age you old git.')
    elif qquestions[i]['answtype'] == 'text' and ans == qquestions[i]['qansw']:
        print('Good guess')
    else:
        print('Wrong!')
