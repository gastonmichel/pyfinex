from ..request import auth_post

# TODO: check query param 'type'
def alert_list(key, secret_key, Type='price', **params):
    """ Get list of alerts
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-alert-list
    """
    endpoint = f'auth/r/alerts?type="{Type}"'
    return auth_post(key, secret_key, 2, endpoint, params=params)

def alert_set(key, secret_key, **params):
    """ Sets up a price alert at the given value
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-alert-set
    """
    endpoint = 'auth/w/alert/set'
    return auth_post(key, secret_key, 2, endpoint, params=params)

def alert_delete(key, secret_key, symbol='tBTCUSD', price=600,**params):
    """ Deletes a price alert
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-alert-delete
    """
    endpoint = 'auth/w/alert/price:{symbol}:{price}/del'
    return auth_post(key, secret_key, 2, endpoint, params=params)