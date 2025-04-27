import requests
from bs4 import BeautifulSoup
#url of page
url = 'https://www.utrgv.edu/csci/faculty/index.htm'
#sending http request
response = requests.get(url)

if response.status_code == 200:
    print("Web page fetched successfully!")
else:
    print("Failed to get the page. Status code:", response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
listings = soup.find_all('div', {"class": "listing"})
for l in listings:
    link = l.find("a", href=lambda h: h and h.startswith("mailto:"))
    if link:
        email = link["href"].split(":", 1)[1]
        print(email)