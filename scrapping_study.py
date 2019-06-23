# Imports
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests
import time
import re
import scrapy
from scrapy.crawler import CrawlerProcess




headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
"""
Some websites automatically block any kind of scraping, and that’s why I’ll define a header to pass along the get command, 
which will basically make our queries to the website look like they are coming from an actual browser. When we run the program, 
I’ll have a sleep command between pages, so we can mimic a “more human” behavior and don’t overload the site with several requests per second. 
You will get blocked if you scrape too aggressively, so it’s a nice policy to be polite while scraping.
"""
# Getting the URL from the website, with the real estate from Odivelas
sapo = 'https://casa.sapo.pt/comprar-apartamentos/odivelas/?sa=11'

# Creating the get request to the website
sapo_response = requests.get(sapo, headers=headers)
sapo_response = sapo_response

# Checking the contents of the response we got from the website
# print(sapo_response.text[:1000])

# Creating the Beautiful Soup object that will help me read the html
soup = BeautifulSoup(sapo_response.text, 'html.parser')

# page_containers = soup.find_all('div', class_='searchContent')
# print(page_containers)

house_containers = soup.find_all('div', class_='searchResultProperty')
# print(house_containers)

# paginador_container = soup.find_all('div', class_='paginador')
# print(paginador_container)

# Finding the first house in the website located in Odivelas
first_house = house_containers[0]
# print(first_house)
#print(first_house.find_all('span'))
#print(len(first_house.find_all('span')))

#prices = []

#price = first_house.find_all('span')
#price_position = int(len(price) - 1)
#price = first_house.find_all('span')[price_position].text
#price_ = [int(price[s]) for s in range(0, len(price)) if price[s].isdigit()]
#price = ''
#for x in price_:
#   price = price + str(x)
#prices.append(int(price))
#
#print(prices)

# print(prices)
# Retrieving the price of the first house

# Now we will retrive a number of characteristics of the first house
# 1) The Location
# location_first = first_house.find_all('p', class_="searchPropertyLocation")[0].text
# 2) The useful area of the apartment
# useful_Area = first_house.find_all('p')[7]
# print(useful_Area)
# 3) Posted date
# date = first_house.find_all('div', class_="searchPropertyDate")
# print(date) # This is returning empty, maybe the site owners decided to take this information out.
# 4) House description
# description = first_house.find_all('p', class_="searchPropertyDescription")[0].text.strip()
# print(description)
# 5) The link
# for url in first_house.find_all('a'):
#     print(url.get('href'))
# 6) The title
# título = first_house.find_all('span')[1].text
# título = título.strip()
# print(título)
# 7) The status
# status = first_house.find_all('p')
# print(status)
# Fixing the link, so that it can used to access the webpage that contains the requested house
# I will be getting rid of the first forward slash and the last 6 digits/letters
link = 'https://casa.sapo.pt/' + first_house.find_all('a')[0].get('href')[1:-6]
print(link)
#request = requests.get(link, headers=headers)
#page_html = BeautifulSoup(request.text, 'html.parser')
#features = str(page_html.find_all('p', class_="ownerName"))
#features = (features[features.find('<p class="ownerName">')+25:features.find('<span class="ownerAMI">')]).strip()
#print(features)

# 6) Fetching the image
# image = str(first_house.find_all('img'))
# print(image)
# final_image = image[image.find('data-src-retina=')+16:image.find('id=')-1]
# print(final_image)