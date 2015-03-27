"""
Geocoding and Web APIs Project Toolbox exercise
Find the MBTA stops closest to a given location.
Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    f = {'address':place_name}
    url_values = urllib.urlencode(f)
    full_url = GMAPS_BASE_URL + '?' + url_values
    response_data = get_json(full_url)
    latitude = response_data['results'][0]['geometry']['location']['lat']
    longitude = response_data['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url_values = urllib.urlencode({'lat': latitude, 'lon': longitude, 'format':json})
    full_url = MBTA_BASE_URL + '?api_key=' + MBTA_DEMO_API_KEY + '&' + url_values
    info = get_json(full_url)
    distance = info['stop'][0]['distance']
    stop_name = info['stop'][0]['stop_name']
    return stop_name + ' is ' + distance + ' miles away.'


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    location = get_lat_long(place_name)
    latitude = location[0]
    longitude = location[1]
    return get_nearest_station(latitude, longitude)

print find_stop_near('Fenway Park')