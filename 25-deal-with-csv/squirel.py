import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_to_dict = data.to_dict()
gray_squirels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirels = data[data["Primary Fur Color"] == "Black"]
# df = data_to_dict["Age"]

data_dict = {
    "Fur Color": [
        "Gray", "Cinnamon", "Black"
    ],
    "Count": [
        len(gray_squirels), len(cinnamon_squirels), len(black_squirels)
    ]}
df = pandas.DataFrame(data_dict)
df.to_csv("squirel_new_csv")
