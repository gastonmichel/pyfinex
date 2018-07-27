from ..api import request

def platform_status(**params):
    """ Get the current status of the platform. 
    Maintenance periods last for just few minutes and might be necessary 
    from time to time during upgrades of core components of our infrastructure.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-platform-status
    """
    endpoint = 'platform/status'
    return request(authenticate=False, version=2, endpoint=endpoint, method='GET', query_params=params)

def tickers(**params):
    """ The ticker is a high level overview of the state of the market. 
    It shows you the current best bid and ask, as well as the last trade price. 
    It also includes information such as daily volume and how much the price has moved over the last day.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-tickers
    """
    endpoint = 'tickers'
    return request(authenticate=False, version=2, endpoint=endpoint, method='GET', query_params=params)

def ticker(Symbol='tBTCUSD', **params):
    """ The ticker is a high level overview of the state of the market. 
    It shows you the current best bid and ask, as well as the last trade price. 
    It also includes information such as daily volume and how much the price has moved over the last day.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-ticker
    """
    endpoint = f'ticker/{Symbol}'
    return request(authenticate=False, version=2, endpoint=endpoint, method='GET', query_params=params)

def trades(Symbol='tBTCUSD', **params):
    """ Trades endpoint includes all the pertinent details of the trade, such as price, size and time.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-trades
    """
    endpoint = f'trades/{Symbol}/hist'
    return request(authenticate=False, version=2, endpoint=endpoint, method='GET', query_params=params)

def books(Symbol='tBTCUSD', Precision='P0', **params):
    """ The Order Books channel allow you to keep track of the state of the Bitfinex order book. 
    It is provided on a price aggregated basis, with customizable precision.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-books
    """
    endpoint = f'book/{Symbol}/{Precision}'
    return request(authenticate=False, version=2, endpoint=endpoint, method='GET', query_params=params)

def stats(Key='pos.size', Size='1m', Symbol='tBTCUSD', Side='long', Section='hist',**params):
    """ Various statistics about the requested pair.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-stats
    """
    endpoint = f'stats1/{Key}:{Size}:{Symbol}/{Section}'
    return request(authenticate=False, version=2, endpoint=endpoint, method='GET', query_params=params)

def candles(Symbol='tBTCUSD', TimeFrame='1m', Section='last', **params):
    """ Various statistics about the requested pair.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-candles
    """
    endpoint = f'candles/trade:{TimeFrame}:{Symbol}/{Section}'
    return request(authenticate=False, version=2, endpoint=endpoint, method='GET', query_params=params)
    
### REST CALCULATION ENDPOINTS ###############################################
def market_avg_price(**params):
    """ Calculate the average execution rate for Trading or Margin funding.
    Docs: https://bitfinex.readme.io/v2/reference#rest-calc-market-average-price
    """
    endpoint = 'calc/trade/avg'
    return request(authenticate=False, version=2, endpoint=endpoint, method='POST', query_params=params)

def forex_rate(**params):
    """ Calculate the Foreign Exchange Rate
    Docs: https://bitfinex.readme.io/v2/reference#foreign-exchange-rate
    """
    endpoint = 'calc/fx'
    return request(authenticate=False, version=2, endpoint=endpoint, method='POST', body_params=params)
