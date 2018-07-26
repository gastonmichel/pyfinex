from ..request import auth_post

def active(key, secret_key, **params):
    """ Get active positions
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-positions
    """
    endpoint = 'auth/r/positions'
    return auth_post(key, secret_key, 2, endpoint, params=params)