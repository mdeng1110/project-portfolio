import requests
from bs4 import BeautifulSoup

#fetch the website content.  Make a HTTP GET request to URL of the product page.
url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)

#check if the request was successful
if response.status_code == 200:
    page_content = response.text
    soup = BeautifulSoup(page_content, "html.parser")
    #check how to find the price
    price_element = soup.find("span",class_="a_price")
else:
    print(f"Failed to fetch content form {url}")
    exit()

