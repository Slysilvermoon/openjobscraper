### This module will is directly calling the Dice API for job search and intercepting the JSON file

import requests
from UAgent import UAgent ## random useragent will be pulled from this module
import json

UA = UAgent.UserAgent()
#print(UA)

## headers variable for dice API
headers = {'User-Agent': UA,'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://www.dice.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers',
        'x-api-key': '1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8'}


class dice_Scraper:
    def __init__(self, url):
        self.url = url
    
    def jobList(self):
        diceJobs = []
        payload={}
        response = requests.request("GET", self.url, headers=headers, data=payload)
        res = response.json()
        data = res['data']
        if len(data) == 0:
            pass
        else:
            for item in data:
                title = item['title']
                company = item['companyName']
                try:
                    location = item['jobLocation']['displayName']
                except:
                    location = 'Information available in the Job Page'
                try: 
                    salary = item['salary']
                except:
                    salary = 'Not mentioned'
                pageURL = item['detailsPageUrl']
                job = { 
                    'Job Title': title,
                    'Company': company,
                    'Location': location,
                    'Salary': salary,
                    'Job Board': 'Dice'
                }
            diceJobs.append(job)
        
        return diceJobs


