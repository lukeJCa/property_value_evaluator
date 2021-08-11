import requests
from bs4 import BeautifulSoup
import re
import time
from web_address_scanner import fill_datafiles
from singleurl_data_extractor import basic_info
from web_address_consolidator import combine_prices_and_links
import pandas as pd


the_url = "https://www.domain.com.au/sale/perth-region-wa/house/?price=440000-450000&page=1"


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

df = combine_prices_and_links().values.tolist()
cols = ["Link", "Price", "Beds", "Bathrooms", "Carports", "Size", "Type"]
result_df = pd.DataFrame(columns = cols)
result_list = []
for vals in df:
	address = vals[0]
	price = vals[1]
	new_info = basic_info(address)
	if new_info != -1:
		row = [address,price] + new_info
		print(row)
		result_list.append(row)

		df = pd.DataFrame(result_list, columns = cols)
		df.to_csv("data/base_info/current.csv", index=False)
