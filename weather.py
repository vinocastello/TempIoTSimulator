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
        self.__timestamp = datetime.datetime.now()
    
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
        return self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')

    def show(self):
        print(f"Temperature: {self.__temp} °C\nTemp range: {self.__min_temp} - {self.__max_temp}°C\nPressure: {self.__pressure} Pa\nHumidity: {self.__humidity}%")

def get_weather(loc):
    my_api_key = "05ee991c43ccaeba6a9221e4c2b2b5da"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LOCATION[0]}&lon={LOCATION[1]}&appid={my_api_key}"
    res = requests.get(url)
    data = res.json()
    return WEATHER_DATA(data)