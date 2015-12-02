import urllib

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
        Period is a string (i.e. '1d') and interval is an int (i.e. 60)
        See readme.md for examples of usage and more detailed explanation.
        """

        params = {"q":self.symbol, "i":str(interval), "p":period, "f":"d,c,h,l,o,v"}
        encoded_params = urllib.urlencode(params)
        api_url = '%s%s' % (self.BASE_URL, encoded_params)
