## Fetching your first data set

It actually only takes two lines of code to fetch your first set of weather data.

- The first thing to do is declare a variable to store the URL for the API call. Don't forget to change the station ID if you want to use a different Weather Station.

    ``` python
    url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/505307'
    ```

- Next, you can make the call to the API:

    ``` python
    weather = get(url).json()
    ```

- That's it. Save and run your program, then switch over to the Python shell and type `weather` to see the data you have downloaded.

