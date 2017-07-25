from requests import get
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'

pages = 1
weather = get(url).json()
data = weather['items']

while 'next' in weather and pages < 9:    
    url = weather['next']['$ref']
    print('Fetching {0}'.format(url))
    weather = get(url).json()
    data += weather['items']
    pages += 1

temperatures = [record['ambient_temp'] for record in data]
timestamps = [parser.parse(record['reading_timestamp']) for record in data]

#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(timestamps, temperatures)
plt.ylabel('Temperature')
plt.xlabel('date and time')
#plt.gcf().autofmt_xdate()
plt.show()
