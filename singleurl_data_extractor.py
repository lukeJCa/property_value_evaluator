import requests
from bs4 import BeautifulSoup
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Contains functions to provide:
#    Bedrooms
#    Bathrooms
#    Carports
#    Property Type
#    Address
#    Land size
# This information should be formatted and store in a "basic info" table before further
#    data is gathered
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Of the four bits of information returned, must ensure that:
#    The first three are between 0 and 15
#    The fourth has the letter "m" in it
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_info_validity(info):
	confirmed_data = []

	try:
		beds = int(info[0])
		if beds > -1 and beds < 15:
			confirmed_data.append(beds)
	except:
		confirmed_data.append(-1)

	try:
		bathrooms = int(info[1])
		if bathrooms > -1 and bathrooms < 15:
			confirmed_data.append(bathrooms)
	except:
		confirmed_data.append(-1)

	try:
		carports = int(info[2])
		if carports > -1 and carports < 15:
			confirmed_data.append(carports)
	except:
		carports = -1

	try: 
		if "m²" in info[3]:
			confirmed_data.append(int(info[3].strip("m²").replace(',', '')))
		else:
			confirmed_data.append(-1)
	except:
		confirmed_data.append(-1)
	if len(confirmed_data) == 4:
		return confirmed_data
	else:
		return -1

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
# Given a URL, pull the basic info (Above)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def basic_info(url):
	page = requests.get(url)

	if str(page) != "<Response [200]>":
		print(str(page))
		return 1
	else:
		soup = BeautifulSoup(page.content, 'html.parser')
		data = soup.find_all('span', attrs = {'data-testid' : "property-features-text-container"})
		base_info = []
		for line in data[0:4]:
			base_info.append(find_between_r(str(line), 'property-features-text-container">', "<!-- -->"))
		cleaned_info = check_info_validity(base_info)

		list_val = data = soup.find_all('div', attrs = {'data-testid' : "listing-summary-property-type"}) 
		type_info = find_between_r(str(list_val), 'span class="css-in3yi3">', "</span></div>]")

		print(cleaned_info)
		if cleaned_info != -1:
			cleaned_info.append(type_info)

	return cleaned_info

"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# TEST SUITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
	basic_info("https://www.domain.com.au/20-oceanside-promenade-mullaloo-wa-6027-2017044101")

"""
