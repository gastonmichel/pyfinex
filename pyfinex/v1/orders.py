from pyfinex.request import auth_post

def new(key, secret_key, **params):
    """ Submit a new order.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-orders
    """
    endpoint = 'order/new'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def new_multiple(key, secret_key, **params): #TODECIDE: enforce params or not
    """ Submit several new orders at once.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-multiple-new-orders
    """
    endpoint = 'order/new/multi'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def cancel(key, secret_key, **params):
    """ Cancel an order.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-order
    """
    endpoint = 'order/cancel'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def cancel_multiple(key, secret_key, **params):
    """ Cancel multiples orders at once.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-multiple-orders
    """
    endpoint = 'order/cancel/multi'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def cancel_all(key, secret_key, **params):
    """ Cancel multiples orders at once.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-all-orders
    """
    endpoint = 'order/cancel/all'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def replace(key, secret_key, **params):
    """ Replace an orders with a new one.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-replace-order
    """
    endpoint = 'order/cancel/replace'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def status(key, secret_key, **params):
    """ Get the status of an order. Is it active? Was it cancelled? To what extent has it been executed? etc.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-order-status
    """
    endpoint = 'order/status'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def active(key, secret_key, **params):
    """ View your active orders.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-orders
    """
    endpoint = 'orders'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def history(key, secret_key, **params):
    """ View your active orders.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-orders-history
    """
    endpoint = 'orders/hist'
    return auth_post(key, secret_key, 1, endpoint, params=params)