import pandas
# # import csv
# #
# # with open("weather-data.csv", 'r') as weather_data:
# #     data = csv.reader(weather_data)
# #     next(weather_data)
# #     temperatures = []
# #     for row in data:
# #         temperatures.append(int(row[1]))
# #     print(temperatures)

#
# data = pandas.read_csv("weather-data.csv")
# data_dict = data.to_dict()
# data_json = data.to_json()
# print(data_dict)
# print(type(data))
# # print(type(data["temp"]))
# print(data_json)
#
# data_list = data["temp"].tolist()
# print(data_list)
#
# data_series = data["temp"]
# print(data_series.mean())
#
# print(f"Maximum value: {data_series.max()}")
# max_day = data[data.temp == data_series.max()]
# print(max_day)
#
# monday_temp = data[data.day == "Monday"]
# celcius_temp = monday_temp.temp
# far_temp = (celcius_temp * 1.8) + 32
# print(f"Temp for Monday: {far_temp}")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250611.csv")

colors_sq = data["Primary Fur Color"].value_counts(dropna=False)
print(colors_sq)
colors_sq.to_csv("squirrel_count.csv")
# color_squirrel = pandas.DataFrame.count(data)
# print(color_squirrel)
