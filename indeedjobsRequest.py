##### This module is written to scrape the jobs on Indeed.com, once the URLs are generated, indeed's URLs will be passed on through this module.

import requests  ## Importing Requests module to make HTTP request
from bs4 import BeautifulSoup   ## Importing Beautiful soup to read the response to HTTP request
from UAgent import UAgent
import time

UA = UAgent.UserAgent()


## Declaring the value of a Header that will be sent with an HTTP request, so that website doesn't know that this is a bit 
headers = {
    'User-Agent': UA,
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5'
    } 


class indeed_Scraper():    ## Creating Scraper class to scrape jobs data from Indeed
       
    def __init__(self, url):   ## this class will accept one input in the form of a URL, declaring default __init__ function
        self.url = url

    def jobList(self):  ## jobList method needs to be called within the class indeed_Scraper to get the job search info from indeed
        
        indeedJobs = []    ## declaring the list where the job results from the query will be stored
        res = requests.get(self.url, headers=headers)   ## making the request to the URL and storing the response object in res
        soup = BeautifulSoup(res.content, 'html.parser') ## Using Beautiful soup to read the response object 
        divs = soup.find_all('div', class_='jobsearch-SerpJobCard')   ## Using find all to find the information about Jobs (Title, Salary, link etc)
    

        ## running for loop to go through all the job listing on a given page and collect information about individual jobs
        for item in divs:  
            title = item.find('a').text.strip()  ## information on job title
            company = item.find('span', class_='company').text.strip()  ## information on company name
            try:
                location = item.find('span', class_='location accessible-contrast-color-location').text.strip()
            except:
                location = item.find('div', class_='location accessible-contrast-color-location').text.strip()
            try:
                salary = item.find('span', class_='salaryText').text.strip()  ## information on salary
            except AttributeError:
                salary = 'Not Mentioned'     ## salary information is not present for every listing and therefore used try and except to catch the exception
            #ext_url = item.find('a')['href']
           #pageURL = 'https://indeed.com' + ext_url
         ## creating job dictionary to store the values
            job = {'Job Title': title, 
            'Company': company, 
            'Location': location,
            'Salary': salary,
            'Job Board': 'Indeed'
            }
            ## adding all the dictionaries in the list
            indeedJobs.append(job)

        ## returning the list
        return indeedJobs
    



