"""Hangman Game."""
#  Imports
from random import randint # The Random function
import re # Regular expressions

# The functions
def load_words(word_list):
    "Load all the words from a file into a list"
    word_count = 0
    try:
        word_file = open('sowpods.txt', 'r')
    except IOError:
        print('Error, cannot open file')
        return False
    else:
        for word in word_file:
            word_list.append(word)
            word_count += 1
        word_file.close()
    return word_list, word_count

def get_yn(prompt):
    "Get a response from the user restricted to uppercase Y or N."
    i = True
    while i:
        choice = input('\n'+prompt+' [Y|N] :- ').upper()
        alpha_choice = re.sub(r'[\W|\d]', '', choice)
        alpha_choice = re.sub(r'[^YN]', '', alpha_choice)
        if len(alpha_choice) != 1:
            print('\tYou entered "{}", I only want "Y" or "N", please try a again'.format(choice))
        else:
            i = False
    return alpha_choice

def get_word(w_list, w_count):
    "Get the word for this game"
    w_num = randint(0, (w_count-1))
    return w_list[w_num]

def get_letter(used_letters):
    "Get the user's choice of letter"
    already_used = True
    while already_used:
        i = True
        while i:
            char = input('\nChoose your letter:- ').upper()
            r_char = re.sub(r'[\W|\d]', '', char)
            if r_char == '':
                print('\tI reduced it to "{}" so I couldn\'t find a usable character, again?'.format(r_char))
            elif len(r_char) > 1:
                print('\tI reduced it to "{}" but I only want 1 character please..'.format(r_char))
            elif len(r_char) == 1 and len(char) > 1:
                print('\tI reduced it to "{}".'.format(r_char))
                lett_ok = get_yn('\tShall I take that as your choice?')
                if lett_ok == 'Y':
                    break
            else:
                break
        already_used = False
        for j in used_letters[:]:
            if r_char == j:
                print('\tYou\'ve already tried {}, please try again'.format(r_char))
                already_used = True
    return used_letters.append(r_char)

def check_word(word, word_length, used_letters, found_flag):
    "Print the hangman word, the blanks and the used letters."
    good_letter_count = 0
    used_tries = len(used_letters)
    found_flag = True
    print('\n')
    if used_tries > 0:
        for i in range(word_length):
            try:
                used_letters.index(word[i])
            except ValueError:
                print('_ ', end='')
                found_flag = False
            else:
                print('{} '.format(word[i]), end='')
        for i in range(used_tries):
            if used_letters[i] in word:
                good_letter_count += 1
        if not found_flag:
            print('\n\nYou\'ve got {} tries left'.format(11-used_tries+good_letter_count))
    else:
        for i in range(word_length):
            print('_ ', end='')
            found_flag = False
    return found_flag

def prepare_hangman(w_list, w_count):
    "Prepare to play hangman"
    word = get_word(w_list, w_count)
    used_letters = []
    word_length = len(word)-1
    game_lost = False
    found_flag = False
#    for i in range(word_length):
#        print('{} '.format(word[i]), end='')
    print('\nThe word is {} letters long.\n'.format(word_length))
    while not game_lost and not found_flag:
        found_flag = check_word(word, word_length, used_letters, found_flag)
        if not found_flag:
            get_letter(used_letters)
            print('You\'ve entered {} so far'.format(used_letters))
        else:
            print('\n\n\nCongratulations you got the word!\t{}'.format(word))
            print('You got it in {} tries, the letters you tried were {}.'.format(len(used_letters), used_letters))
        good_letter_count = 0
        for i in range(len(used_letters)):
            if used_letters[i] in word:
                good_letter_count += 1
        if len(used_letters)-good_letter_count == 11:
            game_lost = True
            print('\n\nBad luck you\'ve used up all your chances and you\'re hung')
            print('The word was\t\t{}'.format(word))
            print('The letters you tried were {}.'.format(used_letters))
    return

def main():
    "The main program"
    w_list = []
    success = load_words(w_list)
    w_count = success[-1]
    play = get_yn('So do you want to play hangman then?')
    while play == 'Y':
        prepare_hangman(w_list, w_count)
        play = get_yn('Again?')

main()
