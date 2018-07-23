from pyfinex.request import public_get

def ticker(**params):
    """ Gives innermost bid and asks and information on the most recent trade, as well as high, low and volume of the last 24 hours.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-ticker
    """
    symbol = params.pop('symbol')
    endpoint = f'pubticker/{symbol}'
    return public_get(1, endpoint,  params=params)

def stats(**params):
    """ Various statistics about the requested pair.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-stats
    """
    symbol = params.pop('symbol')
    endpoint = f'stats/{symbol}' 
    return public_get(1, endpoint,params=params)

def funding_book(**params):
    """ Get the full margin funding book.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-fundingbook
    """
    currency = params.pop('currency')
    endpoint = f'lendbook/{symbol}'
    return public_get(1, endpoint,params=params)

def order_book(**params):
    """ Get the full order book.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-orderbook
    """
    symbol = params.pop('symbol')
    endpoint = f'book/{symbol}'
    return public_get(1, endpoint,params=params)

def trades(**params):
    """ Get a list of the most recent trades for the given symbol.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-trades
    """
    symbol = params.pop('symbol')
    endpoint = f'trades/{symbol}'
    return public_get(1, endpoint,params=params)

def lends(**params):
    """ Get a list of the most recent funding data for the given currency: total amount lent and Flash Return Rate (in % by 365 days) over time.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-lends
    """
    currency = params.pop('currency')
    endpoint = f'lends/{currency}'
    return public_get(1, endpoint,params=params)

def symbols(**params):
    """ Get a list of valid symbol IDs.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-symbols
    """
    endpoint = f'symbols'
    return public_get(1, endpoint,params=params)

def symbols_details(**params):
    """ Get a list of valid symbol IDs and the pair details.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-symbol-details
    """
    endpoint = f'symbols_details'
    return public_get(1, endpoint,params=params)