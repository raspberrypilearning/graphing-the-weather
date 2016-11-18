from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'

weather = get(url).json()
data = weather['items']

while 'next' in weather:
    url = weather['next']['$ref']
    print('fetching {0}'.format(url))
    weather = get(url).json()
    data += weather['items']

temperatures = [record['ambient_temp'] for record in data]
timestamps = [parser.parse(record['reading_timestamp']) for record in data]

plt.plot(timestamps, temperatures)
#plt.xlim(min(timestamps),max(timestamps))
plt.show()


