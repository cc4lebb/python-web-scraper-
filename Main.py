import requests
from bs4 import BeautifulSoup as bs
from urls import url_list

response = requests.get(url_list[1])
soup = bs(response.text, 'html.parser')
print(soup)