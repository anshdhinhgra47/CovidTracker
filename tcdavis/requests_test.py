import requests

def getStats(country='USA'):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":country}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "651785a2b8mshf3fabbd82bffb97p166abbjsn6488158095bb"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

def getNews(region='en-US'):
    
    url = "https://microsoft-azure-bing-news-search-v1.p.rapidapi.com/search"

    querystring = {"count":"1","mkt":region,"q":"covid"}

    headers = {
        'x-rapidapi-host': "microsoft-azure-bing-news-search-v1.p.rapidapi.com",
        'x-rapidapi-key': "651785a2b8mshf3fabbd82bffb97p166abbjsn6488158095bb"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.text

def translate(s):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = "format=text&q=string&target=en"
    headers = {
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "651785a2b8mshf3fabbd82bffb97p166abbjsn6488158095bb",
        'accept-encoding': "application/gzip",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text
