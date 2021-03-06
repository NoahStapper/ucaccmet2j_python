# Seattle,WA,GHCND:US1WAKG0038

import json 

with open('precipitation.json', encoding='utf8') as file:  
    data = json.load(file)


#print(data[0]['station'])

seattle_data = 'GHCND:US1WAKG0038'

value_seattle = []
date_seattle = []
for measurement in data:
    if (measurement['station']) == seattle_data:
        value_seattle.append((measurement['value']))
        date_seattle.append((measurement['date'])[5:7])

# weather_dic = dict(zip(date_seattle, value_seattle))
# print(weather_dic)




weather_dic = {}
i = 0
for month in date_seattle:
    if month in weather_dic:
        weather_dic[month] += value_seattle[i]
    else:
        weather_dic[month] = value_seattle[i]
    i += 1
print(weather_dic)


with open('monthly_precipitation.json', 'w', encoding='utf8') as file:  
    json.dump(weather_dic, file)


year_precipiation = sum(value_seattle)
print(year_precipiation)


relative_precipiation = {}
for month in weather_dic:
    relative_precipiation[month] = (weather_dic[month])/year_precipiation
print(relative_precipiation)


with open('relative_precipitation.json', 'w', encoding='utf8') as file:  
    json.dump(relative_precipiation, file)

