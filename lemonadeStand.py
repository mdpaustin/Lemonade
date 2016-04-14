import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

player_pantry = {'day': 1, 'lemon_cups': 0, 'sugar_cups': 0, 'cups_cups': 0, 'cash': 15.00, 'savings': 0, 'signs': 0, 'current': "Sunny and Warm", 'future': ""}

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
    print(Style.BRIGHT + Fore.CYAN +"\nIt is day %d" % player_pantry['day'])
    print(Style.BRIGHT + Fore.CYAN +"\nToday's weather is %s" % player_pantry['current'])
    print(Style.BRIGHT + Fore.CYAN +"Tomorrow's weather looks to be %s" % player_pantry['future'])
    print(Style.BRIGHT + Fore.WHITE +"\nYou have:")
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

def weather():
    def randomizer(): #create a nested function to call the randomizer for generating the future weather states
        weather = ['Sunny','Partly Cloudy','Overcast','Drizzling','Rainy'] #Weather options
        temp = ['Hot','Warm','Cool','Cold'] #Temperature options
        rand_weth = random.choice(weather)
        rand_temp = random.choice(temp)
        return rand_weth, rand_temp
    future_weather_a = ""
    future_weather_b = ""
    future_temp_a = ""
    future_temp_b = ""

    
def input_num2(prompt="How much cash to add: "):
    while True:
        num_str = input(prompt).strip()
        if all(c in '+-.0123456789' for c in num_str):
            break
    if '.' in num_str:
        return float(num_str)
    else:
        return int(num_str)

lem_title()
inventory()


#The following block is for adding money to the player's cash on hand, sections of this will be referenced when creating the supply store.
'''num_str = input_num2()
player_pantry['cash'] = player_pantry['cash'] + num_str
print("%.2f" % player_pantry['cash'])
num_str = input_num2()
player_pantry['cash'] = player_pantry['cash'] + num_str
print("%.2f" % player_pantry['cash'])
'''

'''while player_state != 'exit':  #the game loop
	if player_state = 'exit':
		break
'''