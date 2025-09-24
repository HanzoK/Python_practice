import pandas

fur_colour = []
colour_count = []
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
new_dict = data["Primary Fur Color"].value_counts().to_dict()

print(type(new_dict))
# new_csv = pandas.DataFrame(new_dict)
# new_csv.to_csv("squirrel_count.csv")
