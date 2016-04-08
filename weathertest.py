#work needed here to predict tomorrow's weather, hold that value and then overwrite that onto the current weather when the day increments.

import random
current_weather = weather_a

def weather():
    weather = ['Sunny','Partly Cloudy','Overcast','Drizzling','Rainy'] #Weather options
    temp = ['Hot','Warm','Cool','Cold'] #Temperature options
    weather_a = "Sunny and Warm" #Initial states - may only be required for weather_a
    weather_b = "Rainy and Cold" 
    tomorrow = random.choice(weather) + " and " + random.choice(temp)
    print ("Today's weather report: " + current_weather)
    print ("Tomorrow's weather: ")

def weather_inc():
    if current_weather == weather_a:
        current_weather = weather_b
weather()