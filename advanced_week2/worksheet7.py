"""Activity 1"""

def main():
    'Does the whole thing.  Get tasks from user and print out'
    todo = []
    priority = []
    print(chr(27) + "[2J") # clear screen

    for i in range(3):
        todo.append(input('Enter Task {0}\n>'.format(i)))
        priority.append(input('Enter priority\n>'))
        print(chr(27) + "[2J") # clear screen
    
    for j in range(3):
        print('{0}\t{1}'.format(todo[j], priority[j]))

if __name__ == "__main__":
    main()