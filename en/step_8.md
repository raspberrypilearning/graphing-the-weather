## Getting the time and temperature

Staying in the shell for now, you can experiment a little to see what data you can extract from the dictionary.

- Type the following into the shell to get the first record:

    ``` python
    >>> first_record = weather['items'][0]
    ```

- Now type `first_record` and you should see something like this:

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

- Now go back to your file, so that you can add to your code. To extract all the temperatures from the `weather` data set, you could use a `for` loop to iterate over the data and pick out all the temperature readings. Something like this would work:

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

- Either method is fine. You now need to do the same thing for the timestamps. You could simply write this:

    ``` python
	## list comprehension to get all the timestamps in a list
    timestamps = [record['reading_timestamp'] for record in weather['items']]
    ```

    There's a small problem, though. The date format used by the database is called the ISO 8601 format. This is a little hard to use in Python, so it needs to be changed to a `datetime` object that Python can easily read. You can do this by passing the timestamp into `parser.parse()` before adding it to a list. For instance, try writing the following in the shell:

    ``` python
    >>> parser.parse(weather['items'][0]['reading_timestamp'])
    ```

- You should see a `datetime` object returned. You can add this to your list comprehension now to give the following:

``` python
## list comprehension to get all the temperatures in a list in a readable format
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]
```
