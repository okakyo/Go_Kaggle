import requests
import time

for i in range(50000):
    get=requests.get('https://laisa.info/count.php')
           
    print(get)
    time.sleep(0.5)
print('Done!')
