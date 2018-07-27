from ..api import request

def balance(key, secret_key, **params):
    """ View all of your balance ledger entries.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-balance-history
    """
    endpoint = 'history'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def deposit_withdrawal_movements(key, secret_key, **params):
    """ View your past deposits/withdrawals.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-deposit-withdrawal-history
    """
    endpoint = 'history/movements'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def past_trades(key, secret_key, **params):
    """ View your past trades.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-past-trades
    """
    endpoint = 'mytrades'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def past_fundings(key, secret_key, **params):
    """ View your past fundings trades.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-mytrades-funding
    """
    endpoint = 'mytrades_funding'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)