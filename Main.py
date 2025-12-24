# website to scrape : https://www.jbhifi.com.au/products/apple-airpods-pro-3

import requests

url = "https://www.jbhifi.com.au/products/apple-airpods-pro-3"

response = requests.get(url)
print(response)