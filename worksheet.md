# Graphing the Weather

One thousand weather stations were sent out to schools all over the world, at the beginning of 2016, ready to be assembled and begin collecting global weather data.

![weather station](images/weather_station.jpg)

Each weather station comes equipped with the sensors, shown in the table below

|Sensor Name|Purpose|
|-----------|-------|
|Rain Gauge|Measures the volume of rain falling in millimetres|
|Anemometer|Measures the wind speed in kilometres per hour|
|Wind Vane|Measures the wind direction in degrees|
|Soil Temperature probe|Measures the soil temperature in degrees Celsius|
|Temperature sensor|Measures the air temperature in degrees Celsius|
|Humidity Sensor|Measures the relative humidity of the air as a percentage|
|Pressure Sensor|Measures the atmospheric pressure in Pascals
|Air Quality Sensor|Measures the air quality as a relative percentage|

The weather stations continually monitor the weather and then send their data to an Oracle database, where it is stored and can be accessed.

In this resource you are going to choose a weather station, and then bulk download some weather data from the database for that station. You will then use Python, to draw some graphs to display the weather data.

## Choosing a Weather Station

With a growing number of Weather Stations coming online each week, there are plenty to choose from. You can follow the [Fetching the Weather]() resource to choose a specific weather station close to you if you like, or you could simply use the one provided in the examples provided in this resource.

Here is a list of some of the active weather stations as of November 2016.

INSERT TABLE OF WEATHER STATIONS HERE

## Getting ready

You can download the recorded weather data for an individual weather station quite easily.

This is because the database that all the weather stations upload data to has a RESTful API. This is a method by which you can write code that uses simple HTTP requests (just like a browser) to fetch the data.

To use a RESTful API, you first need to know which URL to target. In this case the URL to use is:

``` html
https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/
```

To the end of this you need to add the id of the weather station. In this resource, we'll be using weather station - `490722`, but you can use any weather station you wish.

1. Open up a Python shell by clicking on `Menu` > `Programming` > `Python 3 (IDLE)`, then create a new file by clicking on `File` > `New File`

1. You're going to need access to three modules for this resource, two of which are not included in the standard Python library, so make sure you've followed the instructions on the [Software]() page of the resource.

1. The `requests` module handles HTTP calls, which we'll need to fetch web-pages. `matplotlib` is a library that allows you to draw graphs in Python. `dateutil` is a module that allows you to convert dates to different formats.

1. Type the following code into your Python file, to import the needed functions and methods.

``` python
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
```

## Fetching your first data set

It actually only takes two lines of code to fetch your first set of weather data.

1. The first thing to do is declare a variable to store the URL for the API call. Don't forget to change the station id, if you want to use a different weather station.

    ``` python
    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'
    ```

1. Next you can make the call to the API.

    ``` python
    weather = get(url).json()
    ```

1. That's it. Save an run your program. Then switch over to the Python shell and type `weather` to see the data you have downloaded.

## Looking at JSON

The data that is printed out when you type `weather` into the shell is in JSON format. JSON stands for JavaScript Object Notation. It's a really handy format to use in Python programs, because it translates directly into Python dictionaries.

A dictionary is a Python data structure consisting of `keys` and `values`. You can look up any `key` in a dictionary and be returned the `value`

If you look at the weather data, you'll notice that the first and last characters are `{` and `}`. So the entire set of data that you have downloaded is a single dictionary. The key you are interested in is called `'items'`

1. In the shell you can get the value of this key by typing the following.

    ``` python
    weather['items']
    ```

1. You should see that this returns a list (surrounded by `[` and `]`, and the list itself contains even more dictionaries. Each of these dictionaries is a `record` from the database, and contains all the weather data recorded at that specific time.

## Getting the time and temperature.

Staying in the shell for now, you can experiment a little to see what data you can extract from the dictionary.

1. Type the following into the shell to get the first record.

    ``` python
    first_record = weather['items'][0]
    ```

1. Now type `first_record` and you should see something like this.

    ``` python
    {'ground_temp': 9.56, 'air_quality': 76.23, 'created_on': '2016-11-17T11:00:01Z', 'created_by': 'JimStation1', 'ambient_temp': 10.99, 'wind_direction': 327.97, 'rainfall': 0, 'updated_by': 'JimStation1', 'air_pressure': 998.6, 'reading_timestamp': '2016-11-17T11:00:01Z', 'updated_on': '2016-11-17T11:07:22.332Z', 'wind_speed': 2.76, 'id': 1681292, 'wind_gust_speed': 8.16, 'weather_stn_id': 490722, 'humidity': 63.72}
    ```

1. This is all the sensor data that was recorded for that specific time. As you can see it is another dictionary, consisting of key:value pairs. If you wanted to find the ambient air temperature specifically, for instance, you could write the following:

    ``` python
    weather['items'][0]['ambient_temp']
    ```

1. Similarly, the temperature would be `[weather['items'][0]['reading_timestamp']`

1. To extract all the temperatures from the `weather` data-set, you could use a `for` loop to iterate over the data and pick out all the temperature readings. Something like this would work:

    ``` python
    temperatures = []
    for record in weather['data']:
        temperature = record['ambient_temp']
        temperatures.append(temperature)
    ```

1. A list comprehension does the same thin, in far fewer lines however.

    ``` python
    temperatures = [record['ambient_temp'] for record in weather['items']]
    ```

1. Either method is fine though. You now need to do the same thing for the time-stamps. You could simply write this:

    ``` python
    timestamps = [record['reading_timestamp'] for record in weather['items']]
    ```

1. There is a small problem though. The date format used by the database is called the ISO 8601 format. This is a little hard to use in Python, so it needs to be changed to a `datetime` object that Python can easily read. You can do this by passing the time-stamp into `parser.parse()` before adding to a list. For instance, try writing the following into the shell.

    ``` python
    parser.parse(weather['items'][0]['reading_timestamp'])
    ```

1. You should see a `datetime` object returned. You can add this to your list comprehension now to give:

``` python
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]
```

## Graphing the data

So far your full code should look like this:

``` python
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser

url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'

weather = get(url).json()

temperatures = [record['ambient_temp'] for record in weather['items']]
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]
```

1. To graph the data, you only need three lines of code. The first to state the two sets of data you are plotting, the second to display the data.

    ``` python
    plt.plot(timestamps, temperatures)
    plt.show()
    ```

1. Save and run your code, and a graph should be displayed.

1. If you want to add labels to your axes, then you could add the an extra two lines.

``` python
plt.plot(timestamps, temperatures)
plt.ylabel('Temperature')
plt.xlabel('Time')
plt.show()
```

And now you have a graph showing Temperature against time. Why not try and use some different sensor measurements and see what your graph looks like.

## What next?

If you were to hop into the shell and type `len(temperatures)` the largest number you would currently receive back is 500. This is because the way the RESTful API works is by returning pages of data with no more than 500 records per page. In [worksheet two](worksheet2.md) you'll learn how to get more records from the database, to give you sensor data from a larger range of dates.
