from pyfinex.request import auth_post

def basket_manage(key, secret_key, **params):
    """ This endpoint is used to manage the creation or destruction of tokens via splitting or merging. For the moment, this is only useful for the bcc and bcu tokens.
    Docs: https://bitfinex.readme.io/v1/reference#basket-manage
    """
    endpoint = 'basket_manage'
    return auth_post(key, secret_key, 1, endpoint, params=params)