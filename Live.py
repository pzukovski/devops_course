def welcome(name):
    return print(f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")

def load_game():

    """enter game number"""

    game=input("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

    try:
           while  int(game)<1 or int(game)>3:
                game=input("game selection should be between 1 and 3, please try again\n")
    except:
           print("please enter numbers only")
           exit()

    """enter difficulty level"""

    difficulty = input("Please choose game difficulty from 1 to 5:\n")

    try:
        while 1>int(difficulty) or int(difficulty)>5:
            difficulty=input("difficulty selection should be between 1 and 5, please try again\n")
    except:
           print("please enter numbers only")
           exit()

    return (game,difficulty)

if __name__ == '__main__':
   welcome("paul")
   load_game()


