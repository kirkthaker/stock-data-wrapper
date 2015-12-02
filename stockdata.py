import urllib
from collections import namedtuple

Data = namedtuple("Data", "dates closes highs lows opens volumes")

class StockData:

    BASE_URL = "http://www.google.com/finance/getprices?"

    def __init__(self, symbol):
        """
        Initialize with a single security, given its symbol
        """
        self.symbol = symbol

    def get_all_data(self, interval, period):
        """
        Returns a Data object that contains the:
        date, close, high, low, open, and volume for the current stock
        over the specified period and number of intervals (each is an array).
        Interval is an int (i.e. 60) and period is a string (i.e. '1d')
        See readme.md for examples of usage and a more detailed explanation.
        """

        dates = []
        close_prices = []
        high_prices = []
        low_prices = []
        open_prices = []
        volumes = []

        params = {"q":self.symbol, "i":str(interval), "p":period, "f":"d,c,h,l,o,v"}
        encoded_params = urllib.urlencode(params)
        api_url = '%s%s' % (self.BASE_URL, encoded_params)

        opened = urllib.urlopen(api_url)
        raw_data = opened.read()

        # split the data into its rows
        # only need data from the 7th row onwards
        split_data = raw_data.split()[8:]

        for row in split_data:
            row = row.split(",")
            dates.append(int(row[0]))
            close_prices.append(float(row[1]))
            high_prices.append(float(row[2]))
            low_prices.append(float(row[3]))
            open_prices.append(float(row[4]))
            volumes.append(int(row[5]))

        return Data(
            dates = dates,
            closes = close_prices,
            highs = high_prices,
            lows = low_prices,
            opens = open_prices,
            volumes = volumes
        )
