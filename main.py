import requests
import os
from apikey import api_key 

class Argument:
  """input"""
  def __init__(self):
    self.function_name = ''
    self.keyword_dic = {'APPID': api_key}

  def add_argument(self, key, value):
    self.keyword_dic[key] = value

def metricConversion(kelvin):
  # kelvin -> C
  celsius = kelvin - 273.15
  #celsius = (fah - 32)/1.8
  return round(celsius)

def print_weather(weather_data):
  weather_description = weather_data["weather"][0]["description"]
  temperature = metricConversion(weather_data["main"]["temp"]) 
  temperature_body = metricConversion(weather_data["main"]["feels_like"])
  humidity = weather_data["main"]["humidity"]
  visibility = weather_data['visibility']

  print('weather_description: '+ weather_description)
  print('temperature in celsius : ' + str(temperature))
  print('feels like in celsius: ' + str(temperature_body))
  print('humidity : ' + str(humidity) + '%')
  print('visibility : ' + str(visibility) + 'meter')


#user interface
def get_input():
  argument = Argument()
  exit_ = False

  quit_ = input("Do you want to exit? Enter [y/n]\n")
  if quit_ == 'y':
    exit_ = True
    return argument, exit_

  cityName = input("Please enter the city name:\n")
  argument.add_argument('q',cityName)
  return argument, exit_

def get_openweather(argument):
  baseUrl = "http://api.openweathermap.org/data/2.5/weather"
  response = requests.get(baseUrl, params=argument.keyword_dic)
  if response.status_code != 404 and  response.status_code != 401:
    weather_data = response.json()
    print_weather(weather_data)
    return True
    #print('weather_description'+ weather_data["weather"]["description"])
  elif response.status_code == 401:
    print('Unauthorized Error')
    return False
  else:
    print('Cannot find this city')
    return False

def available(city):
  argument = Argument()
  argument.add_argument('q',city)
  if get_openweather(argument):
    return 1
  else:
    return 0

if __name__ == '__main__':
  [argument,exit_] = get_input()
  if exit_ == False:
    get_openweather(argument)
  # print(response.status_code)
  # print(response.text)
