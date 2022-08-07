import pandas as pd     # For Data Management
from geopy.geocoders import Nominatim # For geocoding & Revers-geocoding
import overpy  # For searching point of interest and others
from geopy.geocoders import ArcGIS
# Geocoding request via Nominatim
geolocator = Nominatim(user_agent="my_app")

from geopy.geocoders import ArcGIS
# geolocator = Nominatim(user_agent="myapp")
# geolocator.geocode(Address)

def place_finder(addresses):
    # geolocator = Nominatim(user_agent="myapp")
    # geolocator.geocode(addresses)
    geolocator = Nominatim(user_agent="my_app")
    return geolocator.geocode(addresses)

print(place_finder("Oxford University"))

def extract_from_coordinate(coordinates):
    Geo_Place = geolocator.reverse(coordinates)
    return Geo_Place.raw

print(extract_from_coordinate("6.459061, 3.28900"))