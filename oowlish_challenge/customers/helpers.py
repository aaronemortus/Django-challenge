import json, requests
from urllib.parse import urlencode
from django.conf import settings
from django import forms


def get_lat_lng(city):
    """
    Function to get location (latitude and longitude) by address (city)
    """
    api_key = settings.GOOGLE_API_KEY
    url_api = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'key': api_key, 'address': city}
    response = requests.get(url_api, urlencode(params))
    data = response.json()
    output = []
    try:
        latitude = data['results'][0]['geometry']['location']['lat']
        longitude = data['results'][0]['geometry']['location']['lng']
        output.append({
            'latitude': latitude,
            'longitude': longitude,
        })
    except IndexError:
        pass
    return output
