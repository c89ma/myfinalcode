#!/usr/bin/python3 

import requests

# OpenWeatherMap API key
WEATHER_API_KEY = 'API'

# Google Maps API key
GOOGLE_MAPS_API_KEY = 'API'

# Base URLs
WEATHER_BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
DIRECTIONS_BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json'

# List of cities for weather
cities = ['Portland', 'Boise', 'Salt Lake City', 'Cheyenne', 'Denver', 'Colorado Springs']

def get_weather(city):
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'imperial'  # For temperature in Fahrenheit. Use 'metric' for Celsius.
    }
    response = requests.get(WEATHER_BASE_URL, params=params)
    return response.json()

def print_weather(city, temp, weather_description):
    # ANSI escape codes for coloring the output
    RED = '\033[91m'
    GREEN = '\033[92m'
    LIGHT_BLUE = '\033[94m'
    RESET = '\033[0m'

    if temp > 85:
        temp_output = f"{RED}{temp}°F{RESET}"
    elif 70 < temp <= 85:
        temp_output = f"{GREEN}{temp}°F{RESET}"
    else:
        temp_output = f"{LIGHT_BLUE}{temp}°F{RESET}"

    print(f"Weather in {city}: {temp_output} - {weather_description}")

def get_directions(origin, destination):
    params = {
        'origin': origin,
        'destination': destination,
        'key': GOOGLE_MAPS_API_KEY
    }
    response = requests.get(DIRECTIONS_BASE_URL, params=params)
    return response.json()

if __name__ == "__main__":
    # Get weather for each city
    for city in cities:
        weather_data = get_weather(city)
        if weather_data['cod'] == 200:
            temperature = weather_data['main']['temp']
            weather_desc = weather_data['weather'][0]['description'].capitalize()
            print_weather(city, temperature, weather_desc)
        else:
            print(f"Failed to fetch weather data for {city}")

    # Get directions from origin to destination
    directions_data = get_directions('Tacoma, WA', 'Colorado Springs, CO')
    if directions_data.get('status') == 'OK':
        route = directions_data['routes'][0]
        legs = route['legs'][0]

        distance = legs['distance']['text']
        duration = legs['duration']['text']
        start_address = legs['start_address']
        end_address = legs['end_address']

        print(f"\nDirections from {start_address} to {end_address}:")
        print(f"Distance: {distance}")
        print(f"Duration: {duration}")
    else:
        print("Failed to fetch directions")

