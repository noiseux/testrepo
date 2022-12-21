from bs4 import BeautifulSoup
import requests

url = 'https://ciffc.net/en/ext/active-fires'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

soup
