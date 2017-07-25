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

- You can add another line to save the first set of data as a list:

    ``` python
    data = weather['items']
    ```

- Next, you need a `while` loop. This loop should run as long as the `weather` dictionary has a key called `'next'`:

    ``` python
    while 'next' in weather:
    ```

- If there's a `'next'` key, then the new `url` can be found that leads to the second page:

    ``` python
        url = weather['next']['$ref']
    ```

- It might be a good idea to add a little `print` statement in here, just to act as a kind of progress meter. This will tell us which page is being downloaded:

    ``` python
        print('Fetching {0}'.format(url))
    ```

- Then the data can be fetched, just like it was before:

    ``` python
        weather = get(url).json()
    ```

- Lastly, the list within the `weather` dictionary from this page can be added to the original page's data:

    ``` python
        data += weather['items']
    ```

- You can try to save and run this program. If it's taking too long for your liking, you can exit the script (`Ctrl` + `C`) and proceed to the next section.

