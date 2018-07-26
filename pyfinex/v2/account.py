from .. import auth_post

def wallets(key, secret_key, **params):
    """ Get account wallets
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-wallets
    """
    endpoint = 'auth/r/wallets'
    return auth_post(key, secret_key, 2, endpoint, params=params)

def orders(key, secret_key, **params):
    """ Get account wallets
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-wallets
    """
    endpoint = 'auth/r/wallets'
    return auth_post(key, secret_key, 2, endpoint, params=params)