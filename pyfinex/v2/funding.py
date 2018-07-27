from ..api import request


def offers_active(key, secret_key, Symbol='fUSD', **params):
    """ Get active funding offers.
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-funding-offers
    """
    endpoint = f'r/funding/offers/{Symbol}'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def offers_hist(key, secret_key, Symbol='fUSD', **params):
    """ Get past inactive funding offers. Limited to last 3 days.
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-funding-offers-hist
    """
    endpoint = f'auth/r/funding/offers/{Symbol}/hist'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def loans(key, secret_key, Symbol='fUSD', **params):
    """ Funds not used in active positions
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-funding-loans
    """
    endpoint = f'auth/r/funding/loans/{Symbol}'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def loans_hist(key, secret_key, Symbol='fUSD', **params):
    """ Inactive funds not used in positions. Limited to last 3 days.
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-funding-loans-hist
    """
    endpoint = f'/auth/r/funding/loans/{Symbol}/hist'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def credits(key, secret_key, Symbol='fUSD', **params):
    """ Funds used in active positions
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-funding-credits
    """
    endpoint = f'auth/r/funding/credits/{Symbol}'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

def credits_hist(key, secret_key, Symbol='fUSD', **params):
    """ Inactive funds used in positions. Limited to last 3 days.
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-funding-credits-hist
    """
    endpoint = f'/auth/r/funding/credits/{Symbol}/hist'
    return request(authenticate=True, key=key, secret_key=secret_key, version=2, endpoint=endpoint, method='POST', body_params=params)

