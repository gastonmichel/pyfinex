from ..api import request

def alert_list(key, secret_key, Type='price', **params):
    """ Get list of alerts
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-alert-list
    """
    endpoint = f'auth/r/alerts?type="{Type}"'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', query_params=params)

def alert_set(key, secret_key, **params):
    """ Sets up a price alert at the given value
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-alert-set
    """
    endpoint = 'auth/w/alert/set'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def alert_delete(key, secret_key, symbol='tBTCUSD', price=600,**params):
    """ Deletes a price alert
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-alert-delete
    """
    endpoint = 'auth/w/alert/price:{symbol}:{price}/del'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)