from pyfinex.request import auth_post

def balance(key, secret_key, **params):
        """ View all of your balance ledger entries.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-balance-history
        """
        endpoint = 'history'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def deposit_withdrawal(key, secret_key, **params):
    """ View your past deposits/withdrawals.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-deposit-withdrawal-history
    """
    endpoint = 'history/movements'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def past_trades(key, secret_key, **params):
    """ View your past trades.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-past-trades
    """
    endpoint = 'mytrades'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def past_fundings(key, secret_key, **params):
    """ View your past fundings trades.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-mytrades-funding
    """
    endpoint = 'mytrades_funding'
    return auth_post(key, secret_key, 1, endpoint, params=params)