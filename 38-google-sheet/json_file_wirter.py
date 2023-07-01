import json 

def write(json_data):
    with open("output.json", "w") as json_file:
        json.dump(json_data, json_file)
