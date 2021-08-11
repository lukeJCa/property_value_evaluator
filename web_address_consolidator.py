from os import listdir
from os.path import isfile, join
import pandas as pd

mypath = "data/web_addresses/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# I want a list which combines the known information into a data frame (price and address)
#    and returns it to the main program.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def combine_prices_and_links():
	result_list = []
	for file in onlyfiles:
		filepath = mypath + file
		with open(filepath, 'r') as f:
			content = f.read().splitlines() 
			price = content[0]
			links = content[1:]
			for link in links:
				result_list.append((link, price))
	result_df = (pd.DataFrame(result_list, columns = ["Link", "Price"]).drop_duplicates(subset=['Link']))
	return result_df
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# TEST 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
	combine_prices_and_links()
"""
