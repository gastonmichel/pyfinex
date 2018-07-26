from ..request import auth_post

def orders(key, secret_key, **params):
    """ Get active orders
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-orders
    """
    endpoint = 'auth/r/orders'
    return auth_post(key, secret_key, 2, endpoint, params=params)

def history(key, secret_key, Symbol='tBTCUSD', **params):
    """ Returns the most recent closed or canceled orders up to circa two weeks ago
    Docs: https://bitfinex.readme.io/v2/reference#orders-history
    """
    endpoint = f'auth/r/orders/{Symbol}/hist'
    return auth_post(key, secret_key, 2, endpoint, params=params)