import requests
from bs4 import BeautifulSoup
import re
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time
from web_address_scanner import fill_datafiles

perth_coords = [-31.954592, 115.860537]
the_url = "https://www.domain.com.au/sale/perth-region-wa/house/?price=440000-450000&page=1"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# In order to return some data about how far from the city center the house is,
#    we take the distance of the house from central perth in metres.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_distance_of_points(coords):
	return geodesic(coords, perth_coords)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Duplicated function, finds string in larger string between two substrings.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Latitude longitude function for an address, some playing may be necessary to ensure the 
#     location is in western australia.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_latlon(address):

	geolocator = Nominatim(user_agent="Property Distance Tracker")
	location = geolocator.geocode(address)
	if location is not None:
		return [location.latitude, location.longitude]
	else:
		return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Firstly fill the web addresses file with all links, then go through these systematically
#     and extract relevant information for each.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
fill_datafiles()