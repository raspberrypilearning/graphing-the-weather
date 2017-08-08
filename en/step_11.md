## Finding more pages

The RESTful API returns a maximum of 500 records on the `getallmeasurements` call, in descending date and time order. If you want to collect more records than this, you're going to need a little more code.

- Start a new Python file (`File` > `New File`) and start with the same lines of code you had before:

    ``` python
    from requests import get
    import matplotlib.pyplot as plt
    from dateutil import parser

    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'

    weather = get(url).json()
    ```

- Save and run the script, and then look again at the weather data by typing `weather` into the shell. Have a look and see if you can see a key called `'next'`. You can look at it on its own by typing `weather['next'] into the shell.

    ``` python
    {'$ref': 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722?page=1'}
    ```

    Here you have another dictionary. It contains a single key called `'$ref'`, and the value of `'$ref'` is the URL of the next data set: the next 500 records. You'll notice that the URL ends with `page=1`.

- Let's try a GET request of this URL. Into the shell, type the following:

    ``` python
    weather2 = get(weather['next']['$ref']).json()
    ```

    If the Weather Station you have chosen has sufficient records, you'll hopefully see that `weather2['next']` gives you another URL to get the next set of records. It also has a `weather2['previous']` to show you the previous URL.

- With this in mind, it's possible to write a program to collect all the data that's available for an individual Weather Station. Be warned, though: some stations have lots of records, and with each API call taking a few seconds, it could be minutes or even hours before your script finishes running.

