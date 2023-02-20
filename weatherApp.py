import requests
import os
from dotenv import load_dotenv
from geopy.geocoders import Nominatim


# insert your OpenWeatherMap API key here
load_dotenv()
mykey = os.getenv('WEATHERKEY')

def get_weather(location, api_key):

    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")
    # entering the location name
    getLoc = loc.geocode(location)
    # query the OpenWeatherMap API, passing the city name and your API key in the URL
    endpoint = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(getLoc.latitude, getLoc.longitude, api_key)
    response = requests.get(endpoint)
    # check for any errors in the response
    if response.status_code >= 400:
        raise Exception('Bad response from server')
    results  = response.json()
    # get the current temperature from the results in Kalvin
    tempK = results["main"]["temp"]
    # Converts to F
    tempF = round((tempK-273.15)*9/5+32, 2)
    return tempF

def main():
    # code goes here
    print("Welcome to the Weather App!")
    loc = input("Location: ")
    print("The weather in %s is " % loc, get_weather(loc, mykey))

if __name__ == '__main__':
    main()