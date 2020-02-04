import requests
import os
import csv
import json
from apikey import api_key 

class Argument:
  """input"""
  def __init__(self):
    self.keyword_open = {'APPID': api_key}

  def add_argument(self, key, value):
    self.keyword_open[key] = value


def metricConversion(kelvin):
  # kelvin -> C
  celsius = kelvin - 273.15
  return round(celsius)

def FConversion(fah):
  # F -> C
  celsius = (fah-32)*5/9
  return round(celsius)


def json_current_weather(data):
  weather = {"main": data["weather"][0]["main"], "description": data["weather"][0]["description"]}
  temp_main = metricConversion(data["main"]["temp"]) 
  temp_body = metricConversion(data["main"]["feels_like"])
  temp = {"temp":temp_main, "feels_like":temp_body,'temperatureUnit':'C'}
  return json.dumps({"weather": weather, "temperature": temp,
    "pressure":data["main"]["pressure"],
    "humidity":data["main"]["humidity"],
    "visibility":data["visibility"],
    "wind":data["wind"]}, sort_keys=True, indent=4)

def json_forecast_weather(forecasts):
  number = forecasts['number']
  name = forecasts['name']
  startTime = forecasts['startTime']
  endTime = forecasts['endTime']
  isDaytime = forecasts['isDaytime']
  temperature = FConversion(forecasts['temperature'])
  temperatureTrend = forecasts['temperatureTrend']
  windSpeed = forecasts['windSpeed']
  windDirection = forecasts['windDirection']
  icon = forecasts['icon']
  shortForecast = forecasts['shortForecast']
  detailedForecast = forecasts['detailedForecast']
  return json.dumps({"number":number, "period":name,
    "Time":{"startTime":startTime,"endTime":endTime,"isDaytime":isDaytime},
    "temperature":{'temperature':temperature,'temperatureUnit':'C','temperatureTrend':temperatureTrend},
    'wind':{'windSpeed':windSpeed,'windDirection':windDirection},
    'icon':icon,'forecast':{'shortForecast':shortForecast,'detailedForecast':detailedForecast}},indent=4)

def airport_info(airport_name):
  with open('data/airports.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row['name'] == airport_name:
        location = {"elevation_ft":row['elevation_ft'], 
        "coordinates":{'latitude_deg':row['latitude_deg'],'longitude_deg':row['longitude_deg']},
        "continent":row['continent'],
        "iso_country":row['iso_country'],
        "iso_region":row['iso_region'],
        "municipality":row['municipality']
        }
        return json.dumps({"ident":row['ident'],"type":row['type'],
          "location":location,"scheduled_service":row["scheduled_service"],
          'code':{'gps_code':row['gps_code'],'iata_code':row['iata_code'],'local_code':row['local_code']},
          'links': {'home_link':row['home_link'],'wikipedia_link':row['wikipedia_link']},
          'keywords':row['keywords']
          },sort_keys=False, indent=4)
    return 0

def get_input(airport_name):
  argument = Argument()
  find = False
  with open('data/airports.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row['name'] == airport_name:
        find = True
        argument.add_argument('lon',row['longitude_deg'])
        argument.add_argument('lat',row['latitude_deg'])
        break;
  return argument,find

def currentWeather(argument):
  baseUrl = "http://api.openweathermap.org/data/2.5/weather"
  response = requests.get(baseUrl, params=argument.keyword_open)
  if response.status_code == 200:
    data = response.json()
    print(json_current_weather(data))
    return True
  elif response.status_code == 401:
    print('Unauthorized Error')
    return False
  else:
    print('Cannot find this airport')
    return False

def forecast(argument):
  baseUrl = "https://api.weather.gov/points/"
  response1 = requests.get(baseUrl + argument.keyword_open['lat'] + ',' + argument.keyword_open['lon'])
  if response1.status_code == 200:
    links = response1.json()
    response2 = requests.get(links['properties']['forecast'])
    if response2.status_code == 200:
      data = response2.json()
      for forecasts in data['properties']['periods']:
        print(json_forecast_weather(forecasts))
      return True
  else:
    print('Cannot find this airport')
    return False

#interface function!
def getCurrentWeather(airport_name):
  argument,find = get_input(airport_name)
  if find:
    if currentWeather(argument):
      return 1
  return 0

#interface function!
def getForecastWeather(airport_name):
  argument,find = get_input(airport_name)
  if find:
    if forecast(argument):
      return 1
  return 0


if __name__ == '__main__':
  print(airport_info('John F Kennedy International Airport'))
  print('-------CURRENT-------')
  getCurrentWeather('John F Kennedy International Airport')
  print('-------FORECAST-------')
  getForecastWeather('John F Kennedy International Airport')
