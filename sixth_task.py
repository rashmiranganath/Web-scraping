import requests  
from bs4 import BeautifulSoup
from pprint import pprint
from fourth_task import more_data

lang_list = []
for i in more_data:
    lang = i["language"]
    lang_list.extend(lang)
# print lang_list

language_dic = {}
i = 0
while i < len(lang_list):
    j = i 
    count = 0
    while j < len(lang_list):
        if lang_list[i]==lang_list[j]:
            count = count + 1
        j = j + 1
        if lang_list[i] not in language_dic:
            var = lang_list[i]
        language_dic[var] = count 
    i = i + 1
print language_dic






