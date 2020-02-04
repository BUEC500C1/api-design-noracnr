import pytest
import weatherAirport

def test_info1():
  assert type(weatherAirport.airport_info('John F Kennedy International Airport')) == str

def test_info2():
  assert weatherAirport.airport_info('BU') == 0

def test_current1():
  assert weatherAirport.getCurrentWeather('John F Kennedy International Airport') == 1

def test_current2():
  assert weatherAirport.getCurrentWeather('Joadsa') == 0

def test_forecast1():
  assert weatherAirport.getForecastWeather('John F Kennedy International Airport') == 1

def test_forecast2():
  assert weatherAirport.getForecastWeather('Joadsa') == 0

