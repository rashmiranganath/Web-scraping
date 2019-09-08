import requests  
from bs4 import BeautifulSoup
from pprint import pprint

mainUrl = "https://www.imdb.com/india/top-rated-indian-movies/"
getData= requests.get(mainUrl)
data = getData.text
print (data)

soup = BeautifulSoup(data,"html.parser")
# print (soup)

tBody = soup.find("tbody",class_="lister-list")
# print (tbody)

tr = tBody.findAll("tr")
# print (tr)

def scrapeTopList(data):
    movieDetailsList = []
    moviePosition = 0
    for i in data:
        movieDetailsDic = {}
        # print (i)
        movieName = i.find("td",class_="titleColumn").a.get_text()
        # print (movieName)
        moviePosition = moviePosition + 1
        # print (moviePosition)
        movieYear = i.find("td",class_="titleColumn").span.get_text()
        # print (movieYear[1:5])
        movieUrlId = i.find("td",class_="posterColumn").a["href"]
        movieUrl = "https://www.imdb.com"+ movieUrlId
        # print (movieUrl)

        movieDetailsDic["name"] = movieName
        movieDetailsDic["year"] = movieYear[1:5]
        movieDetailsDic["position"] = moviePosition
        movieDetailsDic["url"] = movieUrl

        movieDetailsList.append(movieDetailsDic)
    return (movieDetailsList)

briefMovieData = scrapeTopList(tr)
# pprint (briefMovieData)