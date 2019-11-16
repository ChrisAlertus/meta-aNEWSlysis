import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os
import json

# api-endpoint 
URL = 'https://www.theglobeandmail.com/search/'
  
# location given here 
issue = "prostate cancer"
issue = issue.replace(" ", "+")  

# defining a params dict for the parameters to be sent to the API 
PARAMS = {
    'q':issue,
    'mode':'news',
    'page':1
} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in text html format 
soup = BeautifulSoup(r.text, 'html.parser')

# parse out new site base domain
domain = urlparse(URL).netloc
    



def getSearchResultIndex(soupHTML):
    # Getting number of results for the query to establish stop criteria
    totalResults = map(lambda x: x.text, soupHTML.find_all("span", \
        class_="c-micro-text c-micro-text--search"))
    #for resultCount in totalResults:
    resultCountString = list(totalResults)[0]
    resultCountString = resultCountString.replace(",","")
    resultCountString = resultCountString.split(" ")
    foundCurrent = False
    
    # print(resultCountString)
    for token in resultCountString:
        #  Displaying 1-10 of 1,000 results
        if not foundCurrent and "-" in token:
            token = token.split("-")
            pageFirst = int(token[0])
            pageLast = int(token[1])
        else:
            if token.isnumeric():
                totalResults = int(token)
    # print(f"""
    #     This page lists the {pageFirst} to {pageLast} results.
    #     In total there are {totalResults} results.""")
    return pageFirst, pageLast, totalResults


def getGlobeAndMailLinks():
    # api-endpoint 
    URL = 'https://www.theglobeandmail.com/search/'
    
    # location given here 
    issue = "prostate cancer"
    issue = issue.replace(" ", "+")  
    pageNum = 1
    # defining a params dict for the parameters to be sent to the API 
    PARAMS = {
        'q':issue,
        'mode':'news',
        'page': pageNum
    } 
    
    # sending get request and saving the response as response object 
    r = requests.get(url = URL, params = PARAMS) 
    
    # extracting data in text html format 
    soup = BeautifulSoup(r.text, 'html.parser')

    # get indces of results and total results
    _, pageLast, totalResults = getSearchResultIndex(soup)

    # Build dictionary of domain and list of article paths
    globeLinks = {domain:[]}

    while pageLast != totalResults:
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        # extracting data in text html format 
        soup = BeautifulSoup(r.text, 'html.parser')
        # get indces of results and total results
        _, pageLast, totalResults = getSearchResultIndex(soup)

        # Find all hyperlinks on site
        resultLinks = map(lambda x: x.get('href'), soup.find_all("a", \
            class_="c-card__link"))
        
        # Adding links from current page to reference dict
        for i, link in enumerate(resultLinks):
            # print(f"Adding page: {PARAMS['page']}, link {i+1}: {link}")
            globeLinks[domain].append(link)
        
        # iterate to next page
        PARAMS['page']+= 1

    print(f"Final list has {totalResults} links.")
    return globeLinks

globeAndMaiLinks = getGlobeAndMailLinks()

# create folder in ../data/links if not exists
# print the list of links inside
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.absolute()
print(REPO_ROOT)
if not os.path.isdir(f"{REPO_ROOT}/data/links/{domain}"):
    os.mkdir(f"{REPO_ROOT}/data/links/{domain}")

linksJSON = json.dumps(globeAndMaiLinks)
linksFile = open(f"{REPO_ROOT}/data/links/{domain}/links.json",'w')
linksFile.write(linksJSON)
linksFile.close()