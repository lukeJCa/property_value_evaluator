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
# Given a URL, pull the basic info (Above)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def basic_info(url):
	page = requests.get(url)

	if str(page) != "<Response [200]>":
		return 1
	else:
		print(page.content)
		soup = BeautifulSoup(page.content, 'html.parser')
		spans = soup.find_all(itemprop="url")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# TEST SUITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
	basic_info("https://www.domain.com.au/47-viking-road-dalkeith-wa-6009-2016420069")


