from ..request import auth_post

def read(key, secret_key, **params):
    """ Read user settings
    Docs: https://bitfinex.readme.io/v2/reference#user-settings-read
    """
    endpoint = 'auth/r/settings'
    return auth_post(key, secret_key, 2, endpoint, params=params)

def write(key, secret_key, **params):
    """ Write user settings
    Docs: https://bitfinex.readme.io/v2/reference#user-settings-write
    """
    endpoint = 'auth/w/settings/set'
    return auth_post(key, secret_key, 2, endpoint, params=params)
    
def delete(key, secret_key, **params):
    """ Delete user settings.
    Docs: https://bitfinex.readme.io/v2/reference#user-settings-delete
    """
    endpoint = 'auth/w/settings/del'
    return auth_post(key, secret_key, 2, endpoint, params=params)
    