def ticker(**params):
    """ Gives innermost bid and asks and information on the most recent trade, as well as high, low and volume of the last 24 hours.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-ticker
    """
    symbol = params.pop('symbol')
    endpoint = f'pubticker/{symbol}'
    return self.request(endpoint, method='GET', auth=False, params=params)

def stats(**params):
    """ Various statistics about the requested pair.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-stats
    """
    symbol = params.pop('symbol')
    endpoint = f'stats/{symbol}' 
    return self.request(endpoint, method='GET', auth=False, params=params)

def fundingbook(**params):
    """ Get the full margin funding book.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-fundingbook
    """
    currency = params.pop('currency')
    endpoint = f'lendbook/{symbol}'
    return self.request(endpoint, method='GET', auth=False, params=params)

def orderbook(**params):
    """ Get the full order book.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-orderbook
    """
    symbol = params.pop('symbol')
    endpoint = f'book/{symbol}'
    return self.request(endpoint, method='GET', auth=False, params=params)

def trades(**params):
    """ Get a list of the most recent trades for the given symbol.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-trades
    """
    symbol = params.pop('symbol')
    endpoint = f'trades/{symbol}'
    return self.request(endpoint, method='GET', auth=False, params=params)

def lends(**params):
    """ Get a list of the most recent funding data for the given currency: total amount lent and Flash Return Rate (in % by 365 days) over time.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-lends
    """
    currency = params.pop('currency')
    endpoint = f'lends/{currency}'
    return self.request(endpoint, method='GET', auth=False, params=params)

def symbols(**params):
    """ Get a list of valid symbol IDs.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-symbols
    """
    endpoint = f'symbols'
    return self.request(endpoint, method='GET', auth=False, params=params)

def symbol_details(**params):
    """ Get a list of valid symbol IDs and the pair details.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-symbol-details
    """
    endpoint = f'symbols_details'
    return self.request(endpoint, method='GET', auth=False, params=params)