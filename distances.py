import pandas as pd
from landmark_scanner import get_landmark_distances
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
	if location is not None:
		return [location.latitude, location.longitude], str(location).split(",")[1]
	else:
		return -1,-1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# In order to return some data about how far from the city center the house is,
#    we take the distance of the house from central perth in metres.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_distance_of_points(coords):

	if coords != -1:
		return geodesic(coords, perth_coords)
	else:
		return -1

def attach_coords(df):

	coords = []
	for index, row in df.iterrows():
		link = row['Link']
		address = '-'.join(link.split("https://www.domain.com.au/")[1].split("-")[0:-1]).replace('-', ' ')
		try:
			coord, loc = get_latlon(address)
			coords.append(coord)
		except:
			coord.append((-1,-1))
	print(coords)
	return coords

def attach_distances(coord):
	dist = float(str(get_distance_of_points(coord)).strip(" km"))
	landmark_vals = (get_landmark_distances(coord))
	print(dist)
	print(landmark_vals)
	return landmark_vals

if __name__ == '__main__':
	df = pd.read_csv("data/base_info/current.csv")
	# "data/base_info/current.csv"
	attach_coords(df)
	dist_list = []
	loc_list = []
	landmark_vals = []

	loc_list.append(loc)


	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
	# For all the sets return in landmark_vals, suburb and cbd dist, we need to append columns for each
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	df["Airport_Dist"] = [x[0] for x in landmark_vals]
	df["Airport_ID"] = [x[1] for x in landmark_vals]
	df["Highschool_Dist"] = [x[2] for x in landmark_vals]
	df["Highschool_ID"] = [x[3] for x in landmark_vals]
	df["Primaryschool_Dist"] = [x[4] for x in landmark_vals]
	df["Primaryschool_ID"] = [x[5] for x in landmark_vals]
	df["Univeristy_Dist"] = [x[6] for x in landmark_vals]
	df["University_ID"] = [x[7] for x in landmark_vals]
	df["Lake_Dist"] = [x[6] for x in landmark_vals]
	df["Lake_ID"] = [x[7] for x in landmark_vals]
	df["Hospital_Dist"] = [x[8] for x in landmark_vals]
	df["Hospital_ID"] = [x[9] for x in landmark_vals]
	df["Costline_Dist"] = [x[10] for x in landmark_vals]

	df["CBD_Dist"] = dist_list
	df["Suburb"] = loc_list
	print(df)
	df.to_csv("data/base_info/current_with_distance.csv", index=False)