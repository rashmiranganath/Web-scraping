from first_task import briefMovieData
import json

file_name = "file_name.json"
def writeFile(data,file_name):
    json_data = json.dumps(data)
    with open(file_name,"w") as f:
        f.write(json_data)

write_data = writeFile(briefMovieData,file_name)

def readFile(file_name):
    with open(file_name,"r") as f:
        var = f.read()
        # print var
readFile(file_name)