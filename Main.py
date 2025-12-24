import requests
from bs4 import BeautifulSoup as bs
from urls import url_list

for url in url_list:
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    urlAmount = soup.find_all("") #need to find element of html/ css here to print the price from each website
    print(urlAmount)