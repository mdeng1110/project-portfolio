import requests
from bs4 import BeautifulSoup

#fetch the website content.  Make a HTTP GET request to URL of the product page.
url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Find the HTML element that contain the price
price = soup.find(class_="a-offscreen").get_text()

# Remove dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)