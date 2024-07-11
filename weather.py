#!/usr/bin/python3


import requests

# Replace with your own API key from OpenWeatherMap
API_KEY = 'API_Key'

# List of cities you want to get the weather for
cities = ['Portland', 'Boise', 'Salt Lake City', 'Cheyenne', 'Denver', 'Colorado Springs']

# Base URL for the OpenWeatherMap API
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'imperial'  # For temperature in Fahrenheit. Use 'metric' for Celsius.
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def print_weather(city, temp, weather_description):
    # ANSI escape codes for coloring the output
    RED = '\033[91m'
    GREEN = '\033[92m'
    LIGHT_BLUE = '\033[94m'
    RESET = '\033[0m'
    
    if temp > 85:
        temp_output = f"{RED}{temp}°F{RESET}"
    elif 70 < temp <= 84:
        temp_output = f"{GREEN}{temp}°F{RESET}"
    elif temp < 69:
        temp_output = f"{LIGHT_BLUE}{temp}°F{RESET}"
    else:
        temp_output = f"{temp}°F"
    
    print(f"Weather in {city}:")
    print(f"Temperature: {temp_output}")
    print(f"Description: {weather_description}")
    print()

for city in cities:
    weather_data = get_weather(city)
    if weather_data.get('cod') == 200:
        temp = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        print_weather(city, temp, weather_description)
    else:
        print(f"Could not get weather for {city}")
        print(weather_data.get('message'))
        print()

