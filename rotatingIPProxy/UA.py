import requests
import json
from bs4 import BeautifulSoup

url = 'http://www.useragentstring.com/?uas=Opera/9.70%20(Linux%20i686%20;%20U;%20en-us)%20Presto/2.2.0&getJSON=all'
res = requests.get(url)
user_Agent = res.json()
print(user_Agent)