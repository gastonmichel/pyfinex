from ..api import request

def wallets(key, secret_key, **params):
    """ Get account wallets
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-wallets
    """
    endpoint = 'auth/r/wallets'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def margin_info(key, secret_key, Symbol='base', **params):
    """ Get account margin info
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-info-margin
    """
    endpoint = f'auth/r/info/margin/{Symbol}'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def funding_info(key, secret_key, Symbol='fUSD', **params):
    """ Get account funding info
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-info-funding
    """
    endpoint = f'auth/r/info/funding/{Symbol}'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def available_balances(key, secret_key, **params):
    """ Calculate available balance for order/offer
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-calc-bal-avail
    """
    endpoint = 'auth/calc/order/avail'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

# TODO test Currency=None
def ledgers(key, secret_key, Currency='fUSD', **params):
    """ View your past ledger entries.
    Docs: https://bitfinex.readme.io/v2/reference#ledgers
    """
    endpoint = f'auth/r/ledgers/{Currency}/hist' #if Currency else 'auth/r/ledgers/hist'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)
