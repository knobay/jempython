""" The main program run at start up  """

from library.game import Game

def main():
    contestant = input('Enter your name\n> ')
    duration = input('How many questions per game do you want to play?\n> ')
    thegame = Game(contestant, duration)
    thegame.play()

if __name__ == "__main__":
    main()