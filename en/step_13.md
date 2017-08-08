## Limiting the data downloaded

The Weather Stations take a new reading from their sensors every 10 minutes. That's 144 readings every 24 hours, and around 4464 readings a month. If we round this up to 4500, and we know each page of JSON data contains 500 records, then we know that to get a month's worth of data we need about 9 pages of records.

- A simple `pages` variable can be used to make sure we only grab 9 pages of data. Somewhere above the `while` loop, add the following line:

    ``` python
    pages = 1
    ```

- Then alter the `while` loop so it looks like this:

    ``` python
    while 'next' in weather and pages < 9:
    ```

- Then somewhere within the `while` loop, you need to increment `pages`:

    ``` python
        pages += 1
    ```

- Saving and running this code should fetch 9 pages in total. If you type `len(data)` into the shell, you should see the value 4500 returned, assuming the Weather Station you have chosen has been active for over a month.

