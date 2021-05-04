import requests
import json

url = "https://job-search-api-beta.svc.dhigroupinc.com/v1/dice/jobs/search?q=Administrative%20Assistant&locationPrecision=City&adminDistrictCode2=NY&latitude=40.730610&longitude=-73.935242&countryCode2=US&radius=30&radiusUnit=mi&page=1&pageSize=20&facets=employmentType%7CpostedDate%7CworkFromHomeAvailability%7CemployerType%7CeasyApply%7CisRemote&fields=id%7CjobId%7Csummary%7Ctitle%7CpostedDate%7CjobLocation.displayName%7CdetailsPageUrl%7Csalary%7CclientBrandId%7CcompanyPageUrl%7CcompanyLogoUrl%7CpositionId%7CcompanyName%7CemploymentType%7CisHighlighted%7Cscore%7CeasyApply%7CemployerType%7CworkFromHomeAvailability%7CisRemote&culture=en&recommendations=true&interactionId=0&fj=true&includeRemote=true"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Origin': 'https://www.dice.com',
  'Accept-Encoding': 'gzip, deflate, br',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'TE': 'Trailers',
  'x-api-key': '1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8'
}

response = requests.request("GET", url, headers=headers, data=payload)

res = response.json()

data = res['data']

diceJobs = []

for item in data:
    title = item['title']
    company = item['companyName']
    location = item['jobLocation']['displayName']
    try: 
        salary = item['salary']
    except:
        salary = 'Not mentioned'
    pageURL = item['detailsPageUrl']
    
    job = {
        'Job Title': title,
        'Company': company,
        'Location': location,
        'Salary': salary
    }
    diceJobs.append(job)

print(diceJobs)