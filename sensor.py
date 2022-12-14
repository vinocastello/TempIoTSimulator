import weather
import random
import datetime
from sklearn.svm import OneClassSVM
from collections import Counter

class sensorNode:
    def __init__(self,deviceID,percentage_of_error):
        self.__deviceID = deviceID
        self.__temperature = None
        self.__timestamp = None
        self.__birthdate = None
        self.__percentage_of_error = percentage_of_error
        self.__malicious_counter = 0
        self.__valid_counter = 0
        self.__readings = []

    @property
    def deviceID(self):
        return self.__deviceID

    @property
    def temperature(self):
        return self.__temperature
    
    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def birthdate(self):
        return self.__birthdate
    
    @property
    def valid_counter(self):
        return self.__valid_counter

    @property
    def malicious_counter(self):
        return self.__malicious_counter

    @property
    def readings(self):
        return self.__readings

    def start_device(self):
        self.__birthdate = datetime.datetime.now()

    def gather_data(self,wd):
        # self.__temperature = wd.temp
        self.__temperature = wd.get_random_temp(self.__percentage_of_error)
        self.__readings.append(self.__temperature)
        if wd.min_temp <= self.__temperature <= wd.max_temp:
            self.__valid_counter += 1
        else:
            self.__malicious_counter += 1
        self.__timestamp = wd.timestamp
    
    def continous_gather(self,n):
        wd = weather.get_weather(weather.LOCATION)
        for i in range(n):
            self.gather_data(wd)
            print(f"reading {i+1} = {self.temperature}°C")

d1 = sensorNode(1,0.25)
d1.continous_gather(1000)
print(f"valid readings = {d1.valid_counter}")
print(f"invalid readings = {d1.malicious_counter}")
print(f"ratio of invalid to valid = {d1.malicious_counter/d1.valid_counter}")

