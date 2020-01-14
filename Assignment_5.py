# Seattle,WA,GHCND:US1WAKG0038

import json 

with open('precipitation.json', encoding='utf8') as file:  
    data = json.load(file)
print(data)


#print(data[0]['station'])

seattle_data = 'GHCND:US1WAKG0038'

for measurement in data:
    if (measurement['station']) == seattle_data:
        print(measurement['value'])
        print(measurement['date'])

    
    

#print(f'{station}:{(data[0]['GHCND:US1WAKG0038'])}')





