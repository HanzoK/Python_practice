### MANUALLY READING FROM FILE
# with open("weather_data.csv") as file:
#     data = file.readlines()
# stripped_data = []
# for item in data:
#     stripped_item = item.strip()
#     stripped_data.append(stripped_item)

# print(stripped_data)


### USING CSV LIBRARY
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

### USINGPANDAS LIBRARY
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()

# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())

# get data in columns
# print(data["condition"])
# print(data.condition)

# get data in rows
# print(data[data["day"] == "Monday"])

# print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"].temp[0] * (9/5) + 32)

### CREATE A DATAFRAME FROM SCRATCH
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")