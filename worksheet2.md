# Graphing the weather

The RESTful API returns a maximum of 500 records on the `getallmeasurements` call, in descending date and time order. If you want to collect more records than this, you're going to need a little more code.

## Finding more pages

1. Start a new Python file (`File` > `New File`) and start with the same lines of code you had before:

    ``` python
    from requests import get
    import matplotlib.pyplot as plt
    from dateutil import parser

    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'

    weather = get(url).json()
    ```

1. Save and run the script, and then look again at the weather data by typing `weather` into the shell. Have a look and see if you can see a key called `'next'`. You can look at it on its own by typing `weather['next'] into the shell.

    ``` python
    {'$ref': 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722?page=1'}
    ```

    Here you have another dictionary. It contains a single key called `'$ref'`, and the value of `'$ref'` is the URL of the next data set: the next 500 records. You'll notice that the URL ends with `page=1`.

1. Let's try a GET request of this URL. Into the shell, type the following:

    ``` python
    weather2 = get(weather['next']['$ref']).json()
    ```

    If the Weather Station you have chosen has sufficient records, you'll hopefully see that `weather2['next']` gives you another URL to get the next set of records. It also has a `weather2['previous']` to show you the previous URL.

1. With this in mind, it's possible to write a program to collect all the data that's available for an individual Weather Station. Be warned, though: some stations have lots of records, and with each API call taking a few seconds, it could be minutes or even hours before your script finishes running.

## Fetching all the pages

As long as there's a `'next'` key in the weather dictionary, you know there's more data to fetch. You can use this fact to collect all the data.

So far, you should have the following script:

    ``` python
    from requests import get
    import matplotlib.pyplot as plt
    from dateutil import parser

    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'

    weather = get(url).json()
    ```

1. You can add another line to save the first set of data as a list:

    ``` python
    data = weather['items']
    ```

1. Next, you need a `while` loop. This loop should run as long as the `weather` dictionary has a key called `'next'`:

    ``` python
    while 'next' in weather:
    ```

1. If there's a `'next'` key, then the new `url` can be found that leads to the second page:

    ``` python
        url = weather['next']['$ref']
    ```

1. It might be a good idea to add a little `print` statement in here, just to act as a kind of progress meter. This will tell us which page is being downloaded:

    ``` python
        print('Fetching {0}'.format(url))
    ```

1. Then the data can be fetched, just like it was before:

    ``` python
        weather = get(url).json()
    ```

1. Lastly, the list within the `weather` dictionary from this page can be added to the original page's data:

    ``` python
        data += weather['items']
    ```

1. You can try to save and run this program. If it's taking too long for your liking, you can exit the script (`Ctrl` + `C`) and proceed to the next section.

## Limiting the data downloaded

The Weather Stations take a new reading from their sensors every 10 minutes. That's 144 readings every 24 hours, and around 4464 readings a month. If we round this up to 4500, and we know each page of JSON data contains 500 records, then we know that to get a month's worth of data we need about 9 pages of records.

1. A simple `pages` variable can be used to make sure we only grab 9 pages of data. Somewhere above the `while` loop, add the following line:

    ``` python
    pages = 1
    ```

1. Then alter the `while` loop so it looks like this:

    ``` python
    while 'next' in weather and pages < 9:
    ```

1. Then somewhere within the `while` loop, you need to increment `pages`:

    ``` python
        pages += 1
    ```

1. Saving and running this code should fetch 9 pages in total. If you type `len(data)` into the shell, you should see the value 4500 returned, assuming the Weather Station you have chosen has been active for over a month.

## Finishing off with a graph

You can now use the same code from Worksheet One to produce a graph of your data. Your list comprehensions will need to be a little different this time, as you're looking at extracting the temperatures and timestamps from the giant `data` list.

Your entire script should then look something like this:

``` python
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'

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

plt.plot(timestamps, temperatures)
plt.ylabel('Temperature')
plt.xlabel('date and time')
plt.show()
```

## What next?

Have a go at graphing different sensors, and see what patterns you can spot. You can also try accessing different Weather Stations.

Can you plot more than one data set on a graph? Perhaps you could figure out how to plot both wind speed and wind direction, for instance. Maybe you could plot the temperatures from several Weather Stations?



