import pandas as pd     # For Data Management
import overpy  # For searching point of interest and others
import csv
from geopy.geocoders import ArcGIS
from geopy.geocoders import Nominatim  # For geocoding & Revers-geocoding
from geopy import distance
from geopy import Point

# Geocoding request via Nominatim
geolocator = Nominatim(user_agent="myapp")

api = overpy.Overpass()

query = """
    node(around:10000,{lat}, {lon})[{area}];
    (._;>;);
    out body;
    """

def find_poi(lat, lon, area):

    for poi in area:
        result = api.query(query.format(lat=lat, lon=lon, area=poi))
        for node in result.nodes:
            print("Name: %s" % node.tags.get("name", "n/a"))
            print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
        with open(poi + '.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            for node in result.nodes:
                csvwriter.writerow((node.tags.get("name", "n/a"), lat, lon, node.lat, node.lon))


find_poi(6.559061, 3.29788, ['cuisine', 'healthcare', 'shop', 'religion'])

def find_distance(location, poi):
    home = Point(location)
    loc = Point(poi)
    result = distance.distance(home, loc).kilometers
    print("Distance from Home to work", result)


find_distance("6.459061  3.28900", "6.514047  3.377104")

to_way = """
    way({home_lat},  {home_lon}, {poi_lat}, {poi_lon})["highway"];
    (._;>;);
    out body;
    """
def find_way(home_lat, home_lon, poi_lat, poi_lon):

    way_query = api.query(to_way.format(home_lat=home_lat, home_lon=home_lon, poi_lat=poi_lat, poi_lon=poi_lon))
    for way in way_query.ways:
        print("Name: %s" % way.tags.get("name", "n/a"))
        print("  Nodes:")
        for node in way.nodes:
            print("    Lat: %f, Lon: %f" % (node.lat, node.lon))

find_way(6.4768064, 3.275452, 6.559061, 3.29788)
# def find_way(home_lat, home_lon, poi_lat, poi_lon):
#
#     way_query = api.query(to_way.format(home_lat=home_lat, home_lon=home_lon, poi_lat=poi_lat, poi_lon=poi_lon))
#     for way in way_query.ways:
#         print("Name: %s" % way.tags.get("name", "n/a"))
#         print("  Nodes:")
#         for node in way.nodes:
#             print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
#
# find_way(6.4768064, 3.275452, 6.559061, 3.29788)
