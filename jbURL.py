##### This module is written to create URLs for job listings using the pagination and API understanding of different job boards

## Importing urllib to encode the URLs 
import urllib.parse

## Importing lat_long module written to generate the values of latitude and longitude based on city and state provided by the user
import lat_long

## Creating JobUrl class to generate Urls for different job boards that need to be scraped 
class JobUrl:

## init method declaring that JobUrl class needs position, city, and state as input
    def __init__(self, position, city, state):
        self.position = position
        self.city = city
        self.state = state
        self.location = self.city + ',' + ' ' + self.state  ## creating a class variable location 

## method indside JobUrl class that will generate URLs that need to be scraped from indeed for job search
    def indeedUrlGenrtr(self):
    ## creating the list of urls from indeed 
        indeed_url_list = []

    ## url encoding of position variable 
        pos = urllib.parse.quote_plus(self.position)
        loc = urllib.parse.quote_plus(self.location)
    
    ## for loop to generate urls using pagination logic and appending the urls to indeed_url_list
        for page in range(0, 100, 10):
            template = f'https://indeed.com/jobs?q={pos}&l={loc}&start={page}'
            indeed_srch_url = template.format(pos, loc, page)
            indeed_url_list.append(indeed_srch_url) 
        
    ## returning indeed_url_list  
        return indeed_url_list
    
    def diceUrlGenrtr(self):
    ## creating the list of urls from dice
        dice_url_list = []

    ## pulling the value of latitude and longitude
        ltlng_list = lat_long.lat_lng(self.location)
        lat = ltlng_list[0]
        long = ltlng_list[1]

    ## encoding value of position for dice api url
        pos = urllib.parse.quote(self.position)
    
    ## for loop to generate urls using pagination logic and appending the urls to dice_url_list
        for page in range(1, 11):
            template = f"https://job-search-api-beta.svc.dhigroupinc.com/v1/dice/jobs/search?q={pos}&locationPrecision=City&latitude={lat}&longitude={long}&countryCode2=US&radius=30&radiusUnit=mi&page={page}&pageSize=20&facets=employmentType%7CpostedDate%7CworkFromHomeAvailability%7CemployerType%7CeasyApply%7CisRemote&fields=id%7CjobId%7Csummary%7Ctitle%7CpostedDate%7CjobLocation.displayName%7CdetailsPageUrl%7Csalary%7CclientBrandId%7CcompanyPageUrl%7CcompanyLogoUrl%7CpositionId%7CcompanyName%7CemploymentType%7CisHighlighted%7Cscore%7CeasyApply%7CemployerType%7CworkFromHomeAvailability%7CisRemote&culture=en&recommendations=true&interactionId=0&fj=true&includeRemote=true"
            dice_srch_url = template.format(pos, lat, long, page)
            dice_url_list.append(dice_srch_url)

    ## returning dice_url_list
        return dice_url_list



# x = JobUrl('Account Manager', 'Dallas', 'TX').diceUrlGenrtr()
# print(x)







    

