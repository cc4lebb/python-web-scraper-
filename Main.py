import requests
from bs4 import BeautifulSoup as bs
from urls import url_list

for url in url_list:
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    price = soup.find("span", "a-price-whole") #price element

    startOfDomain = url.find('.')
    endOfDomain = url.find(".com")
    domainName = url[startOfDomain + 1:endOfDomain]
    print(f"{domainName}: {price}")



