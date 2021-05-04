
### Importing all the modules that are written to finally assemble in this module
from jbURL import JobUrl
from dicejobsRequest import dice_Scraper
from indeedjobsRequest import indeed_Scraper
import lat_long
import UAgent
from checkurl import checkURL
import time

## class Search 
class Search:

    def __init__(self, position, city, state):
        self.position = position
        self.city = city
        self.state = state
        self.location = city + "," + " " + state
    
    def searchResult(self):
        #urlsIndeed = JobUrl(self.position, self.city, self.state).indeedUrlGenrtr()
        urlsDice = JobUrl(self.position, self.city, self.state).diceUrlGenrtr()
        
        indeedJobs = []
        diceJobs = []
        page = []
        x = 0 
        for url in urlsIndeed:
            paginatedJobsIndeed = indeed_Scraper(url).jobList()
            indeedJobs.append(paginatedJobsIndeed)
            pg = checkURL(url).indeedCheck()
            page.append(pg)
            if x == 0:
                x = x + 1
                time.sleep(2)
                continue
            else:
                if page[x-1] == page[x]:
                    break
                else:
                    pass
                time.sleep(2)
        y = 0
        for url in urlsDice:
            paginatedJobsDice = dice_Scraper(url).jobList()
            diceJobs.append(paginatedJobsDice)
            if y == 0:
                y = y + 1
                time.sleep(2)
                continue
            else:
                if diceJobs[y-1] == diceJobs[y]:
                    break
                else:
                    pass
                time.sleep(2)
        
        jobs = indeedJobs + diceJobs
        return jobs
                


x = Search('Product Manager', 'San Francisco', 'CA').searchResult()

print(x)
