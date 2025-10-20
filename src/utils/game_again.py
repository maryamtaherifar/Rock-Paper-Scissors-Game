from termcolor import cprint

def game_again(scores):

    again = input("Would you like to play again? y/n\n")
    if again.lower() not in ('y', 'n'):
        print('Invalid input!')
        return game_again(scores)
    if again.lower() == 'y':
        return True
    if again.lower() == 'n':
        cprint('Thank you for playing.\nGoodbye!', color='white', on_color='on_blue')
        return False