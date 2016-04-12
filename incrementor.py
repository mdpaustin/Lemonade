import random
global day
day = 0
def incrementor():
    global day
    day = day + 1
    weather = "Sunny"
    return day, weather
    

day, weather = incrementor()
print (day)
print (weather)
incrementor()
print (day)
incrementor()
print (day)