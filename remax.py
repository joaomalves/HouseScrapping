"""
This is a script that performs web scrapping on Portuguese Real Estate agencies.
The main focus is to extract all the houses available in the Odivelas.
Initially this will be performed in Remax website.

Since remax use dynamic content to render their webpages, we will need to use Selenium for that and BeautifulSoup later.
"""

# Imports
from bs4 import BeautifulSoup
#import pandas as pd
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

url = 'https://www.remax.pt/PublicListingList.aspx?SelectedCountryID=12#mode=gallery&tt=261&cr=2&mpts=359,363,364&pt=359&cur=EUR&sb=PriceIncreasing&page=1&sc=12&rl=76&pm=965&lsgeo=76,965,0,0&sid=a81a1d1d-ee36-4236-a72e-31343349c574'

request = requests.get(url, headers=headers)
page_html = BeautifulSoup(request.text, 'html.parser')
#house_containers = page_html.findAll('div', class_='results-container')
house_containers = page_html.findAll('div', attrs={'id':'ll-content-container'})
print(house_containers)
