list = ["rashmi","rahul","ganga","rashmi","rahul"]
list1 = [1,3,4,6,4]
# dic = {}
# i = 0
# while i < len(list):
#     j = i 
#     count = 0
#     while j < len(list):
#         if list[i]==list[j]:
#             count = count + 1
#         j = j + 1
#         if list[i] not in dic:
#             var = list[i]
#         dic[var] = count 
#     i = i + 1
# print dic

new = []
for i in list:
    for j in list1:
        new.append([i,j])
        break
print new
