## Getting ready

You can download the recorded weather data for an individual Weather Station quite easily. This is because the database that all the Weather Stations upload data to has a RESTful API. This is a method by which you can write code that uses simple HTTP requests (just like a browser) to fetch the data.

To use a RESTful API, you first need to know which URL to target. In this case, the URL to use is:

``` html
https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/
```

You need to add the ID of the Weather Station to the end of this. In this resource, we'll be using Weather Station `505307`, but you can use any Weather Station you wish.

- Open up a Python shell by clicking on `Menu` > `Programming` > `Python 3 (IDLE)`, then create a new file by clicking on `File` > `New File`. (The `Menu` is the Raspberry Pi logo in the top-left corner of the screen.)

- You're going to need access to three modules for this resource, two of which are not included in the standard Python library, so make sure you've followed the instructions on the [Software](https://github.com/raspberrypilearning/graphing-the-weather/blob/master/software.md) page of the resource to install them.

    The `requests` module handles HTTP calls, which we'll need to fetch web pages. `matplotlib` is a library that allows you to draw graphs in Python. `dateutil` is a module that allows you to convert dates to different formats.

- Type the following code into your Python file, to import the needed functions and methods:

``` python
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
```

