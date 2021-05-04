import requests
from bs4 import BeautifulSoup

pages =[ ]
x=0
for item in range(600, 700, 10):
    template = f"https://www.indeed.com/jobs?q=Product+Manager&l=Dallas,+TX&start={item}"
    url = template.format(item)
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5'}
    res = requests.get(url, headers=headers)   ## making the request to the URL and storing the response object in res
    soup = BeautifulSoup(res.content, 'html.parser') ## Using Beautiful soup to read the response object 
    pageTag = soup.find('div', id ='searchCountPages').text.strip()
    pageNumber = pageTag[5:7]
    print(pageNumber)
    pages.append(pageNumber)
    if x == 0:
        x = x + 1
        continue
    else:
        if pages[x - 1] == pages[x]:
            #print(pageNumber)
            break
        else:
            pass
    x = x + 1

