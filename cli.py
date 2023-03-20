# credits: github.com/UX-01/cli-arxiv-browser
import requests
from bs4 import BeautifulSoup

url = "https://arxiv.org/list/cs.CR/recent"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
meta_divs = soup.select('div#dlpage > dl > dd > div.meta')

for meta_div in meta_divs:
    list_title_div = meta_div.find('div', {'class': 'list-title mathjax'})
    if list_title_div:
        print(list_title_div.text.strip())
