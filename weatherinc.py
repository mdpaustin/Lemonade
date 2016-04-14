import random

def incrementor():
    day = 0
    day = day + 1
    print(day)
    return day
    
day = incrementor()
print(day)

def weather_inc():
    weather = ['Sunny','Partly Cloudy','Overcast','Drizzling','Rainy'] #Weather options
    temp = ['Hot','Warm','Cool','Cold'] #Temperature options
    future_a = "Sunny and Warm"
    future_b = "Rainy and Cool"
    current = future_a
    tomorrow = future_b

    if current == future_a:
        current = future_b #set current to the next known day
        future_a = random.choice(weather) + " and " + random.choice(temp) #generating new weather prediction for tomorrow
        tomorrow = future_a #sets new weather prediction to tomorrow
    else:
        current = future_a
        future_b = random.choice(weather) + " and " + random.choice(temp)
        tomorrow = future_b
    return current, tomorrow
    
current, tomorrow = weather_inc()