import random

player_state = {'day': 0, 'weather': ""}

def incrementor(player_state):
    def randomizer(): #create a nested function to call the randomizer for generating the future weather states
        weather = ['Sunny','Partly Cloudy','Overcast','Drizzling','Rainy'] #local space weather options for random to pull from
        temp = ['Hot','Warm','Cool','Cold'] #local space temperature options for random to pull from
        rand_weth = random.choice(weather)
        rand_temp = random.choice(temp)
        return rand_weth, rand_temp
    rand_weth, rand_temp = randomizer() #defining variables out of the randomizer function to provide for weather in the incrementor space
    weather = rand_temp + " and " + rand_weth
    player_state['day'] = player_state['day'] + 1
    print ("Day: %d" % player_state['day'])
    print (weather)

#weather = incrementor()
incrementor(player_state)

#print (weather)
incrementor(player_state)

#print (player_state['day'])
incrementor(player_state)

#print (player_state['day'])