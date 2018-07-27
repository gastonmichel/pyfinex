from ..api import request

def read(key, secret_key, **params):
    """ Read user settings
    Docs: https://bitfinex.readme.io/v2/reference#user-settings-read
    """
    endpoint = 'auth/r/settings'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def write(key, secret_key, **params):
    """ Write user settings
    Docs: https://bitfinex.readme.io/v2/reference#user-settings-write
    """
    endpoint = 'auth/w/settings/set'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)
    
def delete(key, secret_key, **params):
    """ Delete user settings.
    Docs: https://bitfinex.readme.io/v2/reference#user-settings-delete
    """
    endpoint = 'auth/w/settings/del'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)
    