import sys,requests,json
from bs4 import BeautifulSoup

BaseUrl='https://www.travel-advisory.info/api?countrycode=IN'

url=requests.get(BaseUrl)
soup=BeautifulSoup(url.content,"lxml")
data=soup.find("p")
print(data)
