import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

perth_coords = [-31.954592, 115.860537]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Latitude longitude function for an address, some playing may be necessary to ensure the 
#     location is in western australia.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_latlon(address):

	geolocator = Nominatim(user_agent="Property Distance Tracker")
	location = geolocator.geocode(address)
	print(location)
	if location is not None:
		return [location.latitude, location.longitude], str(location).split(",")[1]
	else:
		return -1, -1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# In order to return some data about how far from the city center the house is,
#    we take the distance of the house from central perth in metres.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_distance_of_points(coords):
	if coords != -1:
		return geodesic(coords, perth_coords)
	else:
		return -1

if __name__ == '__main__':
	df = pd.read_csv("data/base_info/current.csv")
	print(df)
	dist_list = []
	loc_list = []
	for index, row in df.iterrows():
		link = row['Link']
		address = '-'.join(link.split("https://www.domain.com.au/")[1].split("-")[0:-1]).replace('-', ' ')
		coords, loc = get_latlon(address)
		loc_list.append(loc)
		dist = float(str(get_distance_of_points(coords)).strip(" km"))
		print(dist)
		dist_list.append(dist)
	df["CBD_Dist"] = dist_list
	df["Suburb"] = loc_list
	print(df)
	df.to_csv("data/base_info/current_with_distance.csv", index=False)