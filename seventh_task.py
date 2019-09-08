import requests  
from bs4 import BeautifulSoup
from pprint import pprint
from fourth_task import more_data


director_list = []
for i in more_data:
    director = i["director"]
    director_list.append(director)
# print director_list

director_dic = {}
i = 0
while i < len(director_list):
    j = i
    count = 0
    while j < len(director_list):
        if director_list[i]==director_list[j]:
            count = count + 1
        j = j + 1
        if director_list[i] not in director_dic:
            var = director_list[i]
        director_dic[var] = count 
    i = i + 1
pprint(director_dic)