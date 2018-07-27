from ..api import request

def orders(key, secret_key, **params):
    """ Get active orders
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-orders
    """
    endpoint = 'auth/r/orders'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def history(key, secret_key, Symbol='tBTCUSD', **params):
    """ Returns the most recent closed or canceled orders up to circa two weeks ago
    Docs: https://bitfinex.readme.io/v2/reference#orders-history
    """
    endpoint = f'auth/r/orders/{Symbol}/hist'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)