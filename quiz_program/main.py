""" The main program run at start up  """

from library.game import Game

def main():
    thegame = Game()
    thegame.play()
    print('Score...')
    thegame.announceResults()

if __name__ == "__main__":
    main()