## list comprehension to get all the temperatures in a list in a readable format
timestamps = [parser.parse(record['reading_timestamp']) for record in weather['items']]
```

