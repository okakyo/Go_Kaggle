driver_path='C:\\Users\Kyohei Oka\Downloads\chromedriver.exe'
URL='https://www.anzen.mofa.go.jp/info/pcareahazardinfo_17.html'
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import  By
import re
option=webdriver.ChromeOptions()
option.add_argument('--headless')
driver=webdriver.Chrome(driver_path,options=option)
driver.get(URL)
data=driver.page_source
soup=BeautifulSoup(data,'lxml')
data=soup.find_all('a',href=re.compile("pcinfectionspothazardinfo"))
for name in data:
    print(name.href)
driver.close()
driver.quit()

