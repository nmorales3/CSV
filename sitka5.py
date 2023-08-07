import csv 
from datetime import datetime

infile= open('death_valley_2018_simple.csv','r')
infile= open('sitka_weather_2018_simple.csv','r')
place_name=''
csv_file= csv.reader(infile)

header_row= next(csv_file)

print(header_row)

date_index= header_row.index('DATE')
high_index= header_row.index('TMAX')
low_index= header_row.index('TMIN')
name_index= header_row.index('NAME')

for index, col_header in enumerate(header_row):
    print(index, col_header)

highs= []
dates= []
lows= []



some_date= datetime.strptime('2018-07-01', '%Y-%m-%d')
print(some_date)


for row in csv_file:
    if not place_name:
        place_name=row[name_index]
        print(place_name)
    try:
        some_date= datetime.strptime(row[date_index], '%Y-%m-%d')
        high= int(row[high_index])
        low= int(row[low_index])
        
    except ValueError:
        print(f'Missing data for {some_date}')


    else:
        highs.append(int(row[high_index]))
        lows.append(int(row[low_index]))
        dates.append(some_date)

print(highs[:5])
print(dates[:5])

import matplotlib.pyplot as plt
fig = plt.figure()

fig.autofmt_xdate()


plt.subplot(2,1,1)
# 2 rows, one column, which row youre working on
plt.plot(dates, highs, c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows, facecolor='blue',alpha=0.1)
plt.title(f'{place_name}')


plt.subplot(2,1,2)
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
plt.fill_between(dates,highs,lows, facecolor='blue',alpha=0.1)
plt.title(f'{place_name}')

plt.suptitle('Temperature comparison between Sitka Airport, AK US and Death Valley, CA US')

plt.show()