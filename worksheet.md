# Graphing the weather

One thousand Weather Stations were sent out to schools all over the world at the beginning of 2016, ready to be assembled and begin collecting global weather data.

![Weather Station](images/weather_station.jpg)

Each Weather Station comes equipped with the sensors shown in the table below:

|Sensor Name|Purpose|
|-----------|-------|
|Rain gauge|Measures the volume of rain falling in millimetres|
|Anemometer|Measures the wind speed in kilometres per hour|
|Weathervane|Measures the wind direction in degrees|
|Soil temperature probe|Measures the soil temperature in degrees Celsius|
|Temperature sensor|Measures the air temperature in degrees Celsius|
|Humidity sensor|Measures the relative humidity of the air as a percentage|
|Pressure sensor|Measures the atmospheric pressure in Pascals|
|Air quality sensor|Measures the air quality as a relative percentage|

The Weather Stations continually monitor the weather and then send their data to an Oracle database, where it is stored and can be accessed.

In this resource you're going to choose a Weather Station, and then bulk download some weather data from the database for that station. You will then use Python to draw some graphs to display the weather data.

## Choosing a Weather Station

With a growing number of Weather Stations coming online each week, there are plenty to choose from. You can follow the [Fetching the Weather](https://www.raspberrypi.org/learning/fetching-the-weather/) resource to choose a specific Weather Station close to you if you like, or you could simply use the one provided in the examples in this resource.

Here is a list of some of the IDs of active Weather Stations, as of November 2016:


	490722, 505307, 505367, 506882, 509944, 515967, 519781, 520153, 
	520275, 524920, 526297, 528071, 541759, 552355, 553997, 562837, 586603, 
	586921, 587328, 591441, 595131, 595229, 638013, 667858, 668306, 714944, 
	748308, 860212, 903578, 903675, 906364, 1023840, 1042161, 1073533, 
	1100597, 1101852, 1111673, 1158690, 1195685, 1212453, 1253673, 1261471, 
	1269584, 1307290, 1355086, 1356217, 1373810, 1406723, 1546872, 1551853, 
	1569432, 1569473, 1572018, 1592317, 1598227, 1604642, 1615966, 1621459, 
	1624210, 1648902, 1674106, 1682287, 1683740


## Getting ready

You can download the recorded weather data for an individual Weather Station quite easily. This is because the database that all the Weather Stations upload data to has a RESTful API. This is a method by which you can write code that uses simple HTTP requests (just like a browser) to fetch the data.

To use a RESTful API, you first need to know which URL to target. In this case, the URL to use is:

``` html
https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/
```

You need to add the ID of the Weather Station to the end of this. In this resource, we'll be using Weather Station `505307`, but you can use any Weather Station you wish.

1. Open up a Python shell by clicking on `Menu` > `Programming` > `Python 3 (IDLE)`, then create a new file by clicking on `File` > `New File`. (The `Menu` is the Raspberry Pi logo in the top-left corner of the screen.)

1. You're going to need access to three modules for this resource, two of which are not included in the standard Python library, so make sure you've followed the instructions on the [Software](https://github.com/raspberrypilearning/graphing-the-weather/blob/master/software.md) page of the resource to install them.

    The `requests` module handles HTTP calls, which we'll need to fetch web pages. `matplotlib` is a library that allows you to draw graphs in Python. `dateutil` is a module that allows you to convert dates to different formats.

1. Type the following code into your Python file, to import the needed functions and methods:

``` python
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
```

## Fetching your first data set

It actually only takes two lines of code to fetch your first set of weather data.

1. The first thing to do is declare a variable to store the URL for the API call. Don't forget to change the station ID if you want to use a different Weather Station.

    ``` python
    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'
    ```

1. Next, you can make the call to the API:

    ``` python
    weather = get(url).json()
    ```

1. That's it. Save and run your program, then switch over to the Python shell and type `weather` to see the data you have downloaded.

## Looking at JSON

The data that is printed out when you type `weather` into the shell is in JSON format. JSON stands for JavaScript Object Notation. It's a really handy format to use in Python programs, because it translates directly into Python dictionaries.

A dictionary is a Python data structure consisting of `keys` and `values`. You can look up any `key` in a dictionary and have the `value` returned.

If you look at the weather data, you'll notice that the first and last characters are `{` and `}`, so the entire set of data that you've downloaded is a single dictionary. The key you're interested in is called `'items'`.

1. In the shell you can get the value of this key by typing the following (The `>>>` are there by default):

    ``` python
    >>> weather['items']
    ```

You should see that this returns a list surrounded by `[` and `]`, and the list itself contains even more dictionaries. Each of these dictionaries is a `record` from the database, and contains all the weather data recorded at that specific time.

## Getting the time and temperature

Staying in the shell for now, you can experiment a little to see what data you can extract from the dictionary.

1. Type the following into the shell to get the first record:

    ``` python
    >>> first_record = weather['items'][0]
    ```

1. Now type `first_record` and you should see something like this:

    ``` python
    {'ground_temp': 9.56, 'air_quality': 76.23, 'created_on': '2016-11-17T11:00:01Z',
	'created_by': 'JimStation1', 'ambient_temp': 10.99, 'wind_direction': 327.97,
	'rainfall': 0, 'updated_by': 'JimStation1', 'air_pressure': 998.6,
	'reading_timestamp': '2016-11-17T11:00:01Z', 'updated_on': '2016-11-17T11:07:22.332Z',
	'wind_speed': 2.76, 'id': 1681292, 'wind_gust_speed': 8.16, 'weather_stn_id': 490722,
	'humidity': 63.72}
    ```

    This is all the sensor data that was recorded for that specific time. As you can see, it's another dictionary, consisting of key:value pairs. If you wanted to find the ambient air temperature specifically, for instance, you could write the following:

    ``` python
    >>> weather['items'][0]['ambient_temp']
    ```

   S imilarly, the time and date  would be `[weather['items'][0]['reading_timestamp']`.

1. Now go back to your file, so that you can add to your code. To extract all the temperatures from the `weather` data set, you could use a `for` loop to iterate over the data and pick out all the temperature readings. Something like this would work:

    ``` python
	## Use a for loop to iterate over the temperatures and add to a list
    temperatures = []
    for record in weather['data']:
        temperature = record['ambient_temp']
        temperatures.append(temperature)
    ```

    A list comprehension does the same thing, but in far fewer lines:

    ``` python
	## list comprehension to get all the temperatures in a list
    temperatures = [record['ambient_temp'] for record in weather['items']]
    ```

1. Either method is fine. You now need to do the same thing for the timestamps. You could simply write this:

    ``` python
	## list comprehension to get all the timestamps in a list
    timestamps = [record['reading_timestamp'] for record in weather['items']]
    ```

    There's a small problem, though. The date format used by the database is called the ISO 8601 format. This is a little hard to use in Python, so it needs to be changed to a `datetime` object that Python can easily read. You can do this by passing the timestamp into `parser.parse()` before adding it to a list. For instance, try writing the following in the shell:

    ``` python
    >>> parser.parse(weather['items'][0]['reading_timestamp'])
    ```

1. You should see a `datetime` object returned. You can add this to your list comprehension now to give the following:

``` python
## list comprehension to get all the temperatures in a list in a readable format
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]
```

## Graphing the data

So far, your full code should look like this:

``` python
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'

wsimeather = get(url).json()

temperatures = [record['ambient_temp'] for record in weather['items']]
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]
```

1. To graph the data, you only need three lines of code. The first will state the two sets of data you're plotting, and the second will display the data:

    ``` python
	## create a plot of timestamps against temperature and show it
    plt.plot(timestamps, temperatures)
    plt.show()
    ```

1. Save and run your code, and a graph should be displayed.

1. If you want to add labels to your axes, then you could add the an extra two lines:

    ``` python
    plt.plot(timestamps, temperatures)
	## Set the axis labels
    plt.ylabel('Temperature')
    plt.xlabel('Time')
    plt.show()
    ```

![graph](images/today.png)

And now you have a graph showing temperature against time. Why not try and use some different sensor measurements, and see what your graph looks like?



## What next?

If you were to hop into the shell and type `len(temperatures)`, the largest number you would currently receive back is 500. This is because the way the RESTful API works is by returning pages of data with no more than 500 records per page. In [Worksheet Two](worksheet2.md) you'll learn how to get more records from the database, to give you sensor data from a larger range of dates.
