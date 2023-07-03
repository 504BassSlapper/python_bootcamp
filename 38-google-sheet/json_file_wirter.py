import json 

def write_json(json_data, json_file):
    with open(json_file, "w") as json_file:
        json.dump(json_data, json_file)


def read_json():
    global data
    with open("output.json", "r") as json_file:
         data = json.load(json_file)
    return data
    
    