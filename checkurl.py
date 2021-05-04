import requests
from UAgent import UAgent
from bs4 import BeautifulSoup

UA = UAgent.UserAgent()


## Declaring the value of a Header that will be sent with an HTTP request, so that website doesn't know that this is a bit 
headers = {
    'User-Agent': UA,
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5'
    } 
class checkURL:
    def __init__(self, url):
        self.url = url 
    
    def indeedCheck(self):
        res = requests.get(self.url, headers=headers)   ## making the request to the URL and storing the response object in res
        soup = BeautifulSoup(res.content, 'html.parser') ## Using Beautiful soup to read the response object 
        pageTag = soup.find('div', id ='searchCountPages').text.strip()
        pageNumber = pageTag[5:7]
        return pageNumber
        
    



    #             x = x + 1
    #             continue
    #         else:
    #             if pages[x - 1] == pages[x]:
    #                 #print(pageNumber)
    #                 break
    #             else:
    #                 pass
    #         x = x + 1




    # pass
