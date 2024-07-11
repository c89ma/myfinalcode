#!/usr/bin/python3 

import requests

# Replace with your own Google Maps API key
API_KEY = 'AIzaSyC6V4mvhBct0inPwAYK196j7rwXH-GqjpA'

# Origin and destination
origin = 'Tacoma, WA'
destination = 'Colorado Springs, CO'

# Base URL for the Google Maps Directions API
BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json'

def get_directions(origin, destination):
    params = {
        'origin': origin,
        'destination': destination,
        'key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

directions_data = get_directions(origin, destination)

if directions_data.get('status') == 'OK':
    route = directions_data['routes'][0]
    legs = route['legs'][0]
    
    distance = legs['distance']['text']
    duration = legs['duration']['text']
    start_address = legs['start_address']
    end_address = legs['end_address']
    
    print(f"Directions from {start_address} to {end_address}:")
    print(f"Total Distance: {distance}")
    print(f"Estimated Time: {duration}\n")
    
    print("Summary of the route:")
    for step in legs['steps']:
        instruction = step['html_instructions']
        instruction = instruction.replace('<div style="font-size:0.9em">', ' ').replace('</div>', ' ')
        instruction = instruction.replace('<b>', '').replace('</b>', '')
        instruction = instruction.replace('<wbr/>', '')
        step_distance = step['distance']['text']
        print(f"{instruction} ({step_distance})")
else:
    print(f"Could not get directions: {directions_data.get('status')}")

