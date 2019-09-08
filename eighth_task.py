from fourth_task import more_data 
# from first_task import briefMovieData
import json
import os.path

# print briefMovieData
print more_data[0:10]



# def writeFile(data,file_name):
#     json_data = json.dumps(data)
#     with open(file_name,"w") as f:
#         f.write(json_data)

# def readFile(file_name):
#     with open(file_name,"r") as f:
#         var = f.read()
#         # print var

# url_list = []
# for i in briefMovieData:
#     url = i["url"]
#     split_url = url.split("/")
#     # print split_url
#     last = split_url[4]
#     # print last
#     file_name = last+".json"
#     # print file_name
#     url_list.append(file_name)
#     # print url_list

# i = 0
# while i<len(more_data):
#     j = i    
#     while j<len(url_list):
#         # j = j + 1   
#         data_new = more_data[i]
#         # print i 
#         url_new = url_list[j]
#         # print j
#         # if os.path.exists(url_new):
#         #     readFile(url_new)
#         if 0==0:
#                 writeFile(data_new,url_new)
#         i = i + 1
        

# for i in more_data:
#     for j in range(i,len(more_data)):
#         writeFile(i,j)
#         break
#     i=j

        
        

    


        


    

