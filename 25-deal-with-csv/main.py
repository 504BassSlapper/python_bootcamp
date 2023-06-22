import pandas

data = pandas.read_csv("weather.csv")

# series and dataframe , excel sheet is considered as df
# print(type(data))
# print(data["temp"])
# print(type(data["temp"]))

data_dict = data.to_dict()
data_list = data["temp"].to_list()
avg = sum(data_list) / len(data_list)
# print(data_dict)
print(data_list)
print(avg)
mean = data["temp"].mean()
print(mean)
print()

