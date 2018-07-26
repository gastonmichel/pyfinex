from ..request import public_get, public_post

def platform_status(**params):
    """ Get the current status of the platform. Maintenance periods last for just few minutes and might be necessary 
    from time to time during upgrades of core components of our infrastructure.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-platform-status
    """
    endpoint = 'platform/status'
    return public_get(2, endpoint,  params=params)

def tickers(**params):
    """ The ticker is a high level overview of the state of the market. It shows you the current best bid and ask, as well as the last trade price. It also includes information such as daily volume and how much the price has moved over the last day.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-tickers
    """
    endpoint = 'tickers'
    return public_get(2, endpoint,  params=params)

def ticker(**params):
    """ The ticker is a high level overview of the state of the market. It shows you the current best bid and ask, as well as the last trade price. It also includes information such as daily volume and how much the price has moved over the last day.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-ticker
    """
    endpoint = 'ticker/' + params.pop('Symbol')
    return public_get(2, endpoint,  params=params)

def trades(**params):
    """ Trades endpoint includes all the pertinent details of the trade, such as price, size and time.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-trades
    """
    endpoint = 'trades/' + params.pop('Symbol') + '/hist'
    return public_get(2, endpoint,  params=params)

def books(**params):
    """ The Order Books channel allow you to keep track of the state of the Bitfinex order book. It is provided on a price aggregated basis, with customizable precision.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-books
    """
    endpoint = 'book/' + params.pop('Symbol') + '/' + params.pop('Precision')
    return public_get(2, endpoint,  params=params)

def stats(**params):
    """ Various statistics about the requested pair.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-stats
    """
    endpoint = 'stats1/' + params.pop('Key') + ':' + params.pop('Size') + ':' + params.pop('Symbol') + '/' + params.pop('Section')
    return public_get(2, endpoint,  params=params)

def candles(**params):
    """ Various statistics about the requested pair.
    Docs: https://bitfinex.readme.io/v2/reference#rest-public-candles
    """
    endpoint = 'candles/trade:' + params.pop('TimeFrame') + ':' + params.pop('Symbol') + '/' + params.pop('Section')
    return public_get(2, endpoint,  params=params)

def market_avg_price(**params):
    """ Calculate the average execution rate for Trading or Margin funding.
    Docs: https://bitfinex.readme.io/v2/reference#rest-calc-market-average-price
    """
    endpoint = 'calc/trade/avg'
    return public_post(2, endpoint,  params=params)

# TODO implement post params in body/ test if work in query url
def forex_rate(**params):
    """ Calculate the Foreign Exchange Rate
    Docs: https://bitfinex.readme.io/v2/reference#foreign-exchange-rate
    """
    endpoint = 'calc/fx'
    return public_post(2, endpoint,  params=params)
