import random

def weather():
    def randomizer(): #create a nested function to call the randomizer for generating the future weather states
        weather = ['Sunny','Partly Cloudy','Overcast','Drizzling','Rainy'] #Weather options
        temp = ['Hot','Warm','Cool','Cold'] #Temperature options
        rand_weth = random.choice(weather)
        rand_temp = random.choice(temp)
        return rand_weth, rand_temp
    
    rand_weth, rand_temp = randomizer()
    future_weather_a = rand_weth
    future_temp_a = rand_temp
    
    rand_weth, rand_temp = randomizer()
    future_weather_b = rand_weth
    future_temp_b = rand_temp
    return future_weather_a, future_temp_a, future_weather_b, future_temp_b

future_weather_a, future_temp_a, future_weather_b, future_temp_b = weather()

print(future_weather_a + " and " + future_temp_a)
print(future_weather_b + " and " + future_temp_b)
    

    
    
'''
def weather():
    def randomizer(): #create a nested function to call the randomizer for generating the future weather states
        weather = ['Sunny','Partly Cloudy','Overcast','Drizzling','Rainy'] #Weather options
        temp = ['Hot','Warm','Cool','Cold'] #Temperature options
        rand_weth = random.choice(weather)
        rand_temp = random.choice(temp)
        initial = rand_temp + " and " rand_weth
        return rand_weth, rand_temp, inital
    
    if player_pantry['current'] == weather_a: #is this a global variable? 
        player_pantry['current'] = weather_b  #is this a global variable?
        rand_temp, rand_weth = randomizer()
        weather_a = rand_weth + " and " + rand_temp
        player_pantry['future'] = weather_a
    else:
        player_pantry['current'] = weather_a
        rand_temp, rand_weth = randomizer()
        weather_b = rand_weth + " and " + rand_temp
        player_pantry['future'] = weather_b
    return weather_a, weather_b
'''

'''    
def randomizer(): #create a nested function to call the randomizer for generating the future weather states
    weather = ['Sunny','Partly Cloudy','Overcast','Drizzling','Rainy'] #Weather options
    temp = ['Hot','Warm','Cool','Cold'] #Temperature options
    rand_weth = random.choice(weather)
    rand_temp = random.choice(temp)
    return rand_weth, rand_temp
'''
'''   
rand_temp, rand_weth = randomizer()
print(rand_temp + " and " + rand_weth)
rand_temp, rand_weth = randomizer()
print(rand_temp + " and " + rand_weth)
'''