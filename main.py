"""
Isto é um script para web scrapping de sites de imobiliárias portugueses.
O foco é extrair todos os anúncios de situado no concelho de Odivelas.
Inicialmente vamos testar apenas para o CasaSapo
"""

# Imports
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
"""
Some websites automatically block any kind of scraping, and that’s why I’ll define a header to pass along the get command, 
which will basically make our queries to the website look like they are coming from an actual browser. When we run the program, 
I’ll have a sleep command between pages, so we can mimic a “more human” behavior and don’t overload the site with several requests per second. 
You will get blocked if you scrape too aggressively, so it’s a nice policy to be polite while scraping.
"""
# Getting the URL from the website, with the real estate from Odivelas
sapo = 'https://casa.sapo.pt/comprar-casas/ofertas-recentes/odivelas/?sa=11'

# Creating the get request to the website
sapo_response = requests.get(sapo, headers=headers)
sapo_response = sapo_response

# Checking the contents of the response we got from the website
#print(sapo_response.text[:1000])

# Creating the Beautiful Soup object that will help me read the html
soup = BeautifulSoup(sapo_response.text, 'html.parser')

house_containers = soup.find_all('div', class_='searchResultProperty')
print(house_containers)

paginador_container = soup.find_all('div', class_='paginador')
print(paginador_container)