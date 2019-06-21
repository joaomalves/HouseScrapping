"""
This is a script that performs web scrapping on Portuguese Real Estate agencies.
The main focus is to extract all the houses available in the Odivelas.
Initially this will be performed in CasaSapo website
"""

# Imports
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
"""
Some websites automatically block any kind of scraping, and that’s why I’ll define a header to pass along the get command, 
which will basically make our queries to the website look like they are coming from an actual browser. When we run the program, 
I’ll have a sleep command between pages, so we can mimic a “more human” behavior and don’t overload the site with several requests per second. 
You will get blocked if you scrape too aggressively, so it’s a nice policy to be polite while scraping.
"""

# Now let's build the crawler
# First, i will create the lists that will handle the retrieved data and later will be used to build a Dataframe
titulo = []
preços = []
proprietario = []
area_util = []
area_bruta = []
estado = []
descrição = []
zona = []
freguesia = []
imagem = []
links = []
data_anuncio = []
# From the website, i can see that there are 40 pages with results. We will make the loop go for 75 pages (in case one
# day more houses are put for sale in the website). We will insert a break in the loop in case it finds an empty house container


start = time.time()

n_pages = 0

for page in range(0, 75):
    n_pages += 1
    url = 'https://casa.sapo.pt/comprar-apartamentos/odivelas/?sa=11&pn=' + str(page)
    request = requests.get(url, headers=headers)
    page_html = BeautifulSoup(request.text, 'html.parser')
    house_containers = page_html.find_all('div', class_="searchResultProperty")
    if house_containers != []:
        for container in house_containers:

            # Price
            if len(container.find_all('span')) < 3:
                price = '-'
                preços.append(price)
            else:
                price = container.find_all('span')[2].text
                if price == 'Contacte Anunciante':
                    price = container.find_all('span')[3].text
                price_ = [int(price[s]) for s in range(0, len(price)) if price[s].isdigit()]
                price = ''
                for x in price_:
                    price = price + str(x)
                preços.append(int(price))

            # Location
            location_first = container.find_all('p', class_="searchPropertyLocation")[0].text
            location_first = location_first.strip()
            if ',' not in location_first:
                zona.append(location_first.strip())
                freguesia.append(location_first.strip())
            else:
                zona.append(location_first.split(',')[0].strip())
                freguesia.append(location_first.split(',')[1].strip())

            # Title
            title = container.find_all('span')[1].text
            if title == 'Contacte Anunciante':
                title = container.find_all('span')[0].text
                titulo.append(title.strip())
            else:
                titulo.append(title.strip())

            # Status
            status = container.find_all('p')[5].text
            estado.append(status)

            # Useful Area and total area
            useful_area = container.find_all('p')[7].text
            total_area = container.find_all('p')[9].text
            area_util.append(useful_area)
            area_bruta.append(total_area)

            # URL
            link = 'https://casa.sapo.pt/' + container.find_all('a')[0].get('href')[1:-6].replace("?", "")
            links.append(link)

            # Image
            img = str(container.find_all('img'))
            final_img = img[img.find('data-src-retina=')+16:img.find('id=')-1].replace("\"", "")
            imagem.append(final_img)

            # Description (NEEDS MORE WORK)
            # description = container.find_all('p', class_="searchPropertyDescription")[0].text.strip()

            # Date (NEEDS MORE WORK - I NEED TO GET INTO THE PAGE ITSELF AND RETRIEVE THE DATE)

    else:
        break

end = time.time()
total_time = round((end - start), 2)

print("Just finished scrapping {} pages, containing {} houses and it took {} seconds.".format(n_pages, len(titulo), total_time))