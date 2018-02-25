"""ToDo List"""

todo = []
priority = []
done = 'N'
while done != 'Y':
    x = input("Enter the to do thing:- ")
    todo.append(x)
    y = input("Enter its priority:- ")
    priority.append(y)
    done = input("Done [Y/N]:- ")
    done = done.upper()

for i in range(len(todo)):
    print('the ToDo''s you entered is:- {}, its priority is {}'.format(todo[i],priority[i]))

