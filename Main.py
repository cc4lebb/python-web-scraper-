import requests
from bs4 import BeautifulSoup as bs
from urls import url_list

keyWord = "== $0"


for url in url_list:
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')

    startOfDomain = url.find('.')
    endOfDomain = url.find(".com")
    domainName = url[startOfDomain + 1:endOfDomain]
    print(f"{domainName}: ")




#need to find element of html/ css here to print the price from each website
'''
span, class. use the in operator to extract the text within the html line to find the word price 
'''