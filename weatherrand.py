import random
'''
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
'''
    
def randomizer(): #create a nested function to call the randomizer for generating the future weather states
    weather = ['Sunny','Partly Cloudy','Overcast','Drizzling','Rainy'] #Weather options
    temp = ['Hot','Warm','Cool','Cold'] #Temperature options
    rand_weth = random.choice(weather)
    rand_temp = random.choice(temp)
    return rand_weth, rand_temp
    
rand_temp, rand_weth = randomizer()
print(rand_temp + " and " + rand_weth)
rand_temp, rand_weth = randomizer()
print(rand_temp + " and " + rand_weth)
