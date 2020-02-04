# api-design-noracnr
api-design-noracnr created by GitHub Classroom
Homework Option2

### User Stories
I, a traveller, want to know the information of airport which help me to choose arriving airport.
I, a student who study abroad, want to get the current weather of departure airport and forecast of arriving airport.

### API Comparison
The difference between Weather.gov API and OpenWeatherMAP API.
* authentication: Weather.gov doesn't need api key while OpenWeatherMap need.
* content: Weather.gov provides a lot of relevant links while OpenWeatherMap provides data of current weather.
* Get method: Weather.gov doesn't have ? & after baseUrl while OpenWeatherMap have.

### Preparation
You will need Python 3.6 or greater and [requests](https://requests.readthedocs.io/en/master/) library to run this api.
```bash
# Install requests
pip3 install requests
```
Import weatherAirport.py, this api, in your python code or bash
```python
import weatherAirport
```
and register [Open Weather](https://openweathermap.org/) for API key which should put in api_key of apikey.py as a string.

### Guide
##### Airport Information
Use this function to get information of an airport you want to know
```python
weatherAirport.airport_info('John F Kennedy International Airport')
```
Then you will get a JSON
```json
{
    "ident": "KJFK",
    "type": "large_airport",
    "location": {
        "elevation_ft": "13",
        "coordinates": {
            "latitude_deg": "40.63980103",
            "longitude_deg": "-73.77890015"
        },
        "continent": "NA",
        "iso_country": "US",
        "iso_region": "US-NY",
        "municipality": "New York"
    },
    "scheduled_service": "yes",
    "code": {
        "gps_code": "KJFK",
        "iata_code": "JFK",
        "local_code": "JFK"
    },
    "links": {
        "home_link": "http://www.panynj.gov/CommutingTravel/airports/html/kennedy.html",
        "wikipedia_link": "https://en.wikipedia.org/wiki/John_F._Kennedy_International_Airport"
    },
    "keywords": "Manhattan, New York City, NYC, Idlewild"
}

```
##### Current Weather
Use this function to get current weather of an airport you want to know
```python
weatherAirport.getCurrentWeather('John F Kennedy International Airport')
```
There is an example
```json
{
    "humidity": 81,
    "pressure": 1011,
    "temperature": {
        "feels_like": 1,
        "temp": 5,
        "temperatureUnit": "C"
    },
    "visibility": 16093,
    "weather": {
        "description": "broken clouds",
        "main": "Clouds"
    },
    "wind": {
        "deg": 170,
        "speed": 2.6
    }
}
```
##### Forecast Weather
Use this function to get current weather of an airport you want to know
```python
weatherAirport.getForecastWeather('John F Kennedy International Airport')
```
Return result may like that:
```Json
{
    "number": 1,
    "period": "Overnight",
    "Time": {
        "startTime": "2020-02-04T00:00:00-05:00",
        "endTime": "2020-02-04T06:00:00-05:00",
        "isDaytime": false
    },
    "temperature": {
        "temperature": 6,
        "temperatureUnit": "C",
        "temperatureTrend": null
    },
    "wind": {
        "windSpeed": "6 mph",
        "windDirection": "SE"
    },
    "icon": "https://api.weather.gov/icons/land/night/bkn?size=medium",
    "forecast": {
        "shortForecast": "Mostly Cloudy",
        "detailedForecast": "Mostly cloudy, with a low around 42. Southeast wind around 6 mph."
    }
}
{
    "number": 2,
    "period": "Tuesday",
    "Time": {
        "startTime": "2020-02-04T06:00:00-05:00",
        "endTime": "2020-02-04T18:00:00-05:00",
        "isDaytime": true
    },
    "temperature": {
        "temperature": 11,
        "temperatureUnit": "C",
        "temperatureTrend": "falling"
    },
    "wind": {
        "windSpeed": "6 mph",
        "windDirection": "NW"
    },
    "icon": "https://api.weather.gov/icons/land/day/rain,70/rain,50?size=medium",
    "forecast": {
        "shortForecast": "Very Light Rain Likely",
        "detailedForecast": "Rain likely. Cloudy. High near 51, with temperatures falling to around 48 in the afternoon. Northwest wind around 6 mph. Chance of precipitation is 70%. New rainfall amounts between a tenth and quarter of an inch possible."
    }
}
```

