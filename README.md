# weather_api_python
A three day weather forecast python script.

By city name
API call:
api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
Parameters:
q = city name and country code divided by comma, use ISO 3166 country codes

By city ID
API call:
api.openweathermap.org/data/2.5/forecast?id={city ID}
Parameters:
id = city ID

By geographic coordinates
API call:
api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}
Parameters:
lat, lon coordinates of the location of your interest

By ZIP code
API call:
api.openweathermap.org/data/2.5/forecast?zip={zip code},{country code}
Parameters:
zip = zip code


For more information go here : https://openweathermap.org/api

# Requirements
1. requests = for getting data from the api
2. pyfiglet = for large header
3. termcolor = for header color

# Running Script
Run the file in console using the follwing command : python openweatherapi.py
