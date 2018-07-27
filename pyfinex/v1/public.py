from ..api import request

def ticker(symbol='BTCUSD', **params):
    """ Gives innermost bid and asks and information on the most recent trade, as well as high, low and volume of the last 24 hours.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-ticker
    """
    endpoint = f'pubticker/{symbol}'
    return request(authenticate=False, version=1, endpoint=endpoint, method='GET', query_params=params)

def stats(symbol='BTCUSD', **params):
    """ Various statistics about the requested pair.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-stats
    """
    endpoint = f'stats/{symbol}' 
    return request(authenticate=False, version=1, endpoint=endpoint, method='GET', query_params=params)

def funding_book(currency='USD',**params):
    """ Get the full margin funding book.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-fundingbook
    """
    endpoint = f'lendbook/{currency}'
    return request(authenticate=False, version=1, endpoint=endpoint, method='GET', query_params=params)

def order_book(symbol='BTCUSD', **params):
    """ Get the full order book.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-orderbook
    """
    endpoint = f'book/{symbol}'
    return request(authenticate=False, version=1, endpoint=endpoint, method='GET', query_params=params)

def trades(symbol='BTCUSD', **params):
    """ Get a list of the most recent trades for the given symbol.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-trades
    """
    endpoint = f'trades/{symbol}'
    return request(authenticate=False, version=1, endpoint=endpoint, method='GET', query_params=params)

def lends(currency='USD', **params):
    """ Get a list of the most recent funding data for the given currency: total amount lent and Flash Return Rate (in % by 365 days) over time.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-lends
    """
    endpoint = f'lends/{currency}'
    return request(authenticate=False, version=1, endpoint=endpoint, method='GET', query_params=params)

def symbols(**params):
    """ Get a list of valid symbol IDs.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-symbols
    """
    endpoint = f'symbols'
    return request(authenticate=False, version=1, endpoint=endpoint, method='GET', query_params=params)

def symbols_details(**params):
    
    """ Get a list of valid symbol IDs and the pair details.
    Docs: https://bitfinex.readme.io/v1/reference#rest-public-symbol-details
    """
    endpoint = f'symbols_details'
    return request(authenticate=False, version=1, endpoint=endpoint, method='GET', query_params=params)