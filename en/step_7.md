## Looking at JSON

The data that is printed out when you type `weather` into the shell is in JSON format. JSON stands for JavaScript Object Notation. It's a really handy format to use in Python programs, because it translates directly into Python dictionaries.

A dictionary is a Python data structure consisting of `keys` and `values`. You can look up any `key` in a dictionary and have the `value` returned.

If you look at the weather data, you'll notice that the first and last characters are `{` and `}`, so the entire set of data that you've downloaded is a single dictionary. The key you're interested in is called `'items'`.

- In the shell you can get the value of this key by typing the following (The `>>>` are there by default):

    ``` python
    >>> weather['items']
    ```

You should see that this returns a list surrounded by `[` and `]`, and the list itself contains even more dictionaries. Each of these dictionaries is a `record` from the database, and contains all the weather data recorded at that specific time.

