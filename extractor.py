from bs4 import BeautifulSoup

import requests

website = requests.get('https://www.minecraft.net/en-us/download/server/bedrock')
soup = BeautifulSoup(website.content, 'html.parser')

url=soup.find('a', class_='downloadlink', attrs={"data-platform": "serverBedrockLinux"}).attrs["href"]

r = requests.get(url)

with open("minecraft.zip", 'wb') as f:
    f.write(r.content)
