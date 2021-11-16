import requests
from bs4 import BeautifulSoup
import re
import time
from web_address_scanner import fill_datafiles
from singleurl_data_extractor import basic_info
from web_address_consolidator import combine_prices_and_links
from distances import attach_coords, attach_distances
import pandas as pd
import numpy as np

the_url = "https://www.domain.com.au/sale/perth-region-wa/house/?price=440000-450000&page=1"
dist_headers = ['Airport_Dist', 'Airport_No', 'Highschool_Dist', 'Highschool_No', 'Primaryschool_dist', 'Primaryschool_No', 'UNI_Dist', 'UNI_No', 'Lake_Dist', 'Lake_No', 'Park_Dist', 'Park_No', "Coast"]


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
# Firstly fill the web addresses file with all links, then go through these systematically
#     and extract relevant information for each.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#fill_datafiles()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Get the data currently in the files into a cohesive data structure
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#df = combine_prices_and_links().values.tolist()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Get coordinates for all of the listed addresses and add them to the dataset
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#???????????????????????????????????????????????????????????????????????????????????????????
df = pd.read_csv("data/coordinates_added.csv")[["Link", "Price", "Beds", "Bathrooms", "Carports", "Size", "Type", "Coordinates"]]
cut_df = df[df['Coordinates'] != "-1"]
print(len(cut_df))
#cols = ["Link", "Price", "Beds", "Bathrooms", "Carports", "Size", "Type", "Coordinates"]

#result_df = pd.DataFrame(columns = cols)
result_list = []
for index, vals in cut_df.iterrows():
	try:
		price = vals["Price"]
		new_info = []
		x= float(vals["Coordinates"].split(",")[0].strip("["))
		y = float(vals["Coordinates"].split(",")[1].strip("]"))
		coords = [x,y]
		print(coords)
		new_info = attach_distances(coords)
		result_list.append(new_info)
	except:
		pass

result = pd.concat([cut_df, pd.DataFrame(result_list, columns = dist_headers)], axis=1)
result.to_csv("final_merged.csv", index = False)

#df = pd.read_csv("data/backup.csv")
#df["Coordinates"] = attach_coords(df)
#df.to_csv("data/coordinates_added.csv")

