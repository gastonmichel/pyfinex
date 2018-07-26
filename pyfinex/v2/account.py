from ..request import auth_post

def wallets(key, secret_key, **params):
    """ Get account wallets
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-wallets
    """
    endpoint = 'auth/r/wallets'
    return auth_post(key, secret_key, 2, endpoint, params=params)

def margin_info(key, secret_key, key='base', **params):
    """ Get account margin info
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-info-margin
    """
    endpoint = f'auth/r/info/margin/{key}'
    return auth_post(key, secret_key, 2, endpoint, params=params)

def funding_info(key, secret_key, key='fUSD', **params):
    """ Get account funding info
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-info-funding
    """
    endpoint = f'auth/r/info/funding/{key}'
    return auth_post(key, secret_key, 2, endpoint, params=params)

def available_balances(key, secret_key, **params):
    """ Calculate available balance for order/offer
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-calc-bal-avail
    """
    endpoint = 'auth/calc/order/avail'
    return auth_post(key, secret_key, 2, endpoint, params=params)

# TODO test Currency=None
def ledgers(key, secret_key, Currency=None, **params):
    """ View your past ledger entries.
    Docs: https://bitfinex.readme.io/v2/reference#ledgers
    """
    endpoint = 'auth/r/ledgers/{Currency}/hist' if Currency else 'auth/r/ledgers/hist'
    return auth_post(key, secret_key, 2, endpoint, params=params)
