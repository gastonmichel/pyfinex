from ..api import request

def active(key, secret_key, **params):
    """ Get active positions
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-positions
    """
    endpoint = 'auth/r/positions'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)