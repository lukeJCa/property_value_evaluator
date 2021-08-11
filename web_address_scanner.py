import requests
from bs4 import BeautifulSoup

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luke C
# Fill the web_address file with all current listed houses in url form from domain
# If the programs exits on its own the bounds are not set correctly
#
# Function should exit if the price is above some set value
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fill_datafiles():
	ID = 1
	ID_page = 1
	while True:
		lower_bound = ID*10000
		upper_bound = (ID+1)*10000
		true_value = (lower_bound+upper_bound)/2
		url = "https://www.domain.com.au/sale/perth-region-wa/house/?price=" + str(ID*10000) + "-" + str((ID+1)*10000) + "&page=" + str(ID_page)
		page = requests.get(url)
		print(str(ID_page) + "_" + str(page))

		if str(page) != "<Response [200]>": ## IF weve passed page 51, should never be called on successful operation
			break
		else:
			soup = BeautifulSoup(page.content, 'html.parser')
			spans = soup.find_all(itemprop="url")

			links = []
			for span in spans:
				links.append(find_between_r(str(span), '<link href=',  ' itemprop=').strip('"'))

			if not links: ## empty
				ID += 1
				ID_page = 1
			else:
				with open("data/web_addresses/" + str(ID) + "_" + str(ID_page) + "_content.txt","w+") as f:
					f.write(str(true_value) + "\n")
					for item in links:
						f.write("%s\n" % item)
				ID_page += 1
		
