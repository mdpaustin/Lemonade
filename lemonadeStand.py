from colorama import init
from colorama import Fore, Back, Style
init()

player_pantry = {'lemon_cups': 0, 'sugar_cups': 0, 'cups_cups': 0, 'cash': 15.00, 'savings': 0}

def inventory():
    print("\nYou have:")
    if player_pantry['lemon_cups'] == 1:
        print(Style.BRIGHT + Fore.YELLOW +"%d lemon" % player_pantry['lemon_cups'])
    else:
        print(Style.BRIGHT + Fore.YELLOW + "%d lemons" % player_pantry['lemon_cups'])
    if player_pantry['sugar_cups'] == 1:
        print(Style.BRIGHT + Fore.WHITE + "%d bag of sugar" % player_pantry['sugar_cups'])
    else:
        print(Style.BRIGHT + Fore.WHITE + "%d bags of sugar" % player_pantry['sugar_cups'])
    if player_pantry['cups_cups'] == 1:
        print(Style.BRIGHT + Fore.CYAN + "%d cup\n" % player_pantry['cups_cups'])
    else:
        print(Style.BRIGHT + Fore.CYAN + "%d cups\n" % player_pantry['cups_cups'])
    print(Fore.GREEN + "%.2f in cash" % player_pantry['cash'])
    print("%.2f in savings" % player_pantry['savings'])

inventory()
'''while player_state != 'exit':  #the game loop
	if player_state = 'exit':
		break
'''