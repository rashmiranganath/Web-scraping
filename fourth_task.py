import requests  
from bs4 import BeautifulSoup
from pprint import pprint
import first_task 

def more_details(briefMovieData):
    new_List = []
    for i in briefMovieData:
        # print "hello world"
        new_dict = {}
        # movie = briefMovieData[1]
        movieUrl = i["url"]
        # print movieUrl
        movieGetData = requests.get(movieUrl)
        # print (movieGetData)
        movieSoup = BeautifulSoup(movieGetData.text,"html.parser")
        # print movieSoup

        name = movieSoup.find("div",class_="title_wrapper").h1.get_text()
        # print (name)
        splitList= name.split()
        # print (splitList)
        splitList.remove(splitList[-1])
        # print (splitList)
        movieName = " ".join(splitList)
        # print (movieName)

        director = movieSoup.find("div",class_="credit_summary_item").a.get_text()
        # print (director)


        country = movieSoup.find("div",class_="subtext")
        country_sub = country.findAll("a")
        # print (country_sub)
        movieCountry = country_sub[-1].get_text()
        # print (movieCountry)
        countrySplit = movieCountry.split()
        # print (countrySplit)
        countryMovie = countrySplit[-1]
        # print (countryMovie[1:6])

        posterPic = movieSoup.find("div",class_="poster").a.img["src"]
        # print (posterPic)

        movieBio = movieSoup.find("div",class_="summary_text").get_text().strip()
        # print (movieBio)

        country_sub.remove(country_sub[-1])
        # print (country_sub)
        genreList = [] 

        for i in country_sub:
            # genreList = []
            genre = i.get_text()
            genreList.append(genre)
            # print (genre)
        # genreList = [] 
        # genreList.append(genre)
        genreData = genreList
        # print (genreData)
    



        runTime = movieSoup.find("div",class_="article",id="titleDetails")
        # print (runTime)
        time = runTime.findAll("div",class_="txt-block")
        var = "Runtime:"
        lang = "Language:"
        for i in time:
            var1 = i.get_text()
            # print (var1)
            if var in var1:
                ans = (i).get_text().split()
                # print (ans)
                # for j in ans:
                    # print (j)
                runtime = ans[1]
                # print (runtime)
                run = runtime + "min"
                # print run
            if lang in var1:
                language = i.get_text().split()
                # print language
                language.remove(language[0])
                # print language

        new_dict["name"] = movieName
        new_dict["director"] = director
        new_dict["country"] = countryMovie[1:6]
        new_dict["genre"] = genreData
        new_dict["runtime"] = run
        new_dict["language"] = language
        new_dict["bio"] =  movieBio 
        new_dict["posterUrl"] = posterPic
        # print new_dict


    new_List.append(new_dict)
    print new_List
    # return new_List
more_data = more_details(briefMovieData)
pprint(more_data)

