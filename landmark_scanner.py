import pandas as pd 
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


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
# In order to return some data about how far from the city center the house is,
#    we take the distance of the house from central perth in metres.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_distance_of_points(coord1, coord2):
	try:
		return geodesic(coord1, coord2)
	except:
		return -1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Theres 7 lists we care about for points, load them all in
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def landmark_distances(coord, filename):
	# AIRPORTS
	with open("data/locations/" + str(filename), 'r') as f:
		content = f.read().splitlines() 
		distances = []
		for row in content:
			coord_full = find_between_r(row,"[","]").split(",")
			x_coord = float(coord_full[0])
			y_coord = float(coord_full[1])
			dist = get_distance_of_points([x_coord, y_coord], coord)
			id = row.split(",")[-1]
			distances.append((float(str(dist).strip(" km")), int(id.strip(" "))))
		sorted_by_first = sorted(distances, key=lambda tup: tup[0])
		return sorted_by_first[0][0], sorted_by_first[0][1]

def get_landmark_distances(house_coords):
	airport_dist, airport_id = landmark_distances(house_coords, "airport.txt")
	print("The closest airport is id: " + str(airport_id) + " and the distance is " + str(airport_dist))

	highschool_dist, highschool_id = landmark_distances(house_coords, "highschool.txt")
	print("The closest highschool is id: " + str(highschool_id) + " and the distance is " + str(highschool_dist))

	primaryschool_dist, primaryschool_id = landmark_distances(house_coords, "primary_school.txt")
	print("The closest primary school is id: " + str(primaryschool_id) + " and the distance is " + str(primaryschool_dist))

	university_dist, university_id = landmark_distances(house_coords, "university.txt")
	print("The closest university is id: " + str(university_id) + " and the distance is " + str(university_dist))

	lake_dist, lake_id = landmark_distances(house_coords, "lake.txt")
	print("The closest lake is id: " + str(lake_id) + " and the distance is " + str(lake_dist))

	hospital_dist, hospital_id = landmark_distances(house_coords, "hospitals.txt")
	print("The closest hospital is id: " + str(hospital_id) + " and the distance is " + str(hospital_dist))

	coastline_dist, coastline_id = landmark_distances(house_coords, "coastline.txt")
	print("The distance to the coastline is " + str(coastline_dist))

	return [airport_dist, airport_id, highschool_dist, highschool_id, primaryschool_dist, primaryschool_id, university_dist, university_id, lake_dist, lake_id, hospital_dist, hospital_id, coastline_dist]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# A known problem with these function is that whitespace at the end of the textfiles will break the reading function
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~