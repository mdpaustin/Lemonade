import colorama
from colorama import Fore, Back, Style
colorama.init()

player_pantry = {'lemon_cups': 0, 'sugar_cups': 0, 'cups_cups': 0, 'cash': 15.00, 'savings': 0, 'signs': 0}

def lem_title():
    print(Style.BRIGHT + Fore.YELLOW)
    print(" __                                                      __          __")
    print("/\\ \\                                                    /\\ \\        /\\ \\")
    print("\\ \\ \\         __    ___ ___     ___     ___      __     \\_\\ \\     __\\ \\ \\")
    print(" \\ \\ \\  __  /'__`\\/' __` __`\\  / __`\\ /' _ `\\  /'__`\\   /'_` \\  /'__`\\ \\ \\")
    print("  \\ \\ \\L\\ \\/\\  __//\\ \\/\\ \\/\\ \\/\\ \\L\\ \\/\\ \\/\\ \\/\\ \\L\\.\\_/\\ \\L\\ \\/\\  __/\\ \\_\\")
    print("   \\ \\____/\\ \\____\\ \\_\\ \\_\\ \\_\\ \\____/\\ \\_\\ \\_\\ \\__/.\\_\\ \\___,_\\ \\____\\\\/\\_\\")
    print("    \\/___/  \\/____/\\/_/\\/_/\\/_/\\/___/  \\/_/\\/_/\\/__/\\/_/\\/__,_ /\\/____/ \\/_/")
    print(Style.RESET_ALL)
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
        print(Style.BRIGHT + Fore.CYAN + "%d cup" % player_pantry['cups_cups'])
    else:
        print(Style.BRIGHT + Fore.CYAN + "%d cups" % player_pantry['cups_cups'])
    if player_pantry['signs'] == 1:
        print(Style.BRIGHT + Fore.CYAN + "%d sign\n" % player_pantry['signs'])
    else:
        print(Style.BRIGHT + Fore.CYAN + "%d signs\n" % player_pantry['signs'])


    print(Fore.GREEN + "%.2f in cash" % player_pantry['cash'])
    print("%.2f in savings" % player_pantry['savings'])

lem_title()
inventory()
'''while player_state != 'exit':  #the game loop
	if player_state = 'exit':
		break
'''