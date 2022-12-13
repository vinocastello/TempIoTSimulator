import requests, json
import datetime
import random

# Location of UP AECH
LOCATION = (14.648900271585852, 121.06881775671476)

def KelvinToCelsius(temp):
    return round(temp - 273.15,2)

class WEATHER_DATA:
    def __init__(self,data):
        self.__humidity = data['main']['humidity']
        self.__pressure = data['main']['pressure']
        self.__temp = KelvinToCelsius(data['main']['temp'])
        self.__max_temp = KelvinToCelsius(data['main']['temp_max'])
        self.__min_temp = KelvinToCelsius(data['main']['temp_min'])
        self.__random_temp = round(random.uniform(self.__min_temp,self.__max_temp),2)
        self.__timestamp = data['dt']
        self.__location = data['name']
    
    @property
    def humidity(self):
        return self.__humidity

    @property
    def pressure(self):
        return self.__pressure

    @property
    def temp(self):
        return self.__temp

    @property
    def max_temp(self):
        return self.__max_temp

    @property
    def min_temp(self):
        return self.__min_temp

    @property
    def random_temp(self):
        return self.__random_temp

    @property
    def timestamp(self):
        temp = datetime.datetime.fromtimestamp(self.__timestamp)
        return temp.strftime('%Y-%m-%d %H:%M:%S')

    @property
    def location(self):
        return self.__location

    def show(self):
        print(f"Timestamp: {self.timestamp}\nLocation: {self.__location}\nTemperature: {self.__temp} °C\nTemp range: {self.__min_temp} - {self.__max_temp}°C\nPressure: {self.__pressure} Pa\nHumidity: {self.__humidity}%")

def get_weather(loc):
    my_api_key = "05ee991c43ccaeba6a9221e4c2b2b5da"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LOCATION[0]}&lon={LOCATION[1]}&appid={my_api_key}"
    res = requests.get(url)
    data = res.json()
    return WEATHER_DATA(data)

def get_random_temp(loc,n):
    random_temps = []
    wt = get_weather(loc)
    for i in range(n):
        random_temp = random.uniform(wt.min_temp,wt.max_temp)
        random_temps.append(random_temp)
    return random_temps

get_weather(LOCATION).show()