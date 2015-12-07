# stock-data-wrapper
A Python wrapper for getting stock data from Google Finance.

## Dependencies
1. Backported enum library for Python 2.7

## Examples & explanation

Import all classes:
```python
from stockdata import *
```

The Stock class must be initialized with the stock's symbol:
```python
sec = Stock("GOOG")
```

The important function is get_data, which takes the following parameters:

1. Interval - how many seconds in between data points. Default is 60.
2. Period - the overall time period for which you want data. Default is 1 day.

```python
sec = Stock("GOOG")
data = sec.get_data() # defaults to getting Google's stock data for every minute over the last 24 hours
print data.closes # a list of close prices for each minute
print data.highs # a list of high prices for each minute
print data.volumes # a list of trading volumes for every minute
```
