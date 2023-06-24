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
print(data["temp"].max())

print(data[data.day == "Monday"])

print("Max temperature \n")
print(data[data.temp == data.temp.max()])
print("Min temperature \n")
print(data[data.temp == data.temp.min()])

monday = data[data.day == "Monday"]
condition = monday.condition
temperature = monday.temp
fahrenheit_temp = temperature * 9 / 5 + 32
print(fahrenheit_temp)
print(condition)

student_game_data_dict = {
    "student": ["Alice", "Bob", "Mathew"],
    "score": [76, 59, 90]
}
data = pandas.DataFrame(student_game_data_dict)
data.to_csv("new_data.csv")
