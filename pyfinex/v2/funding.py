from pyfinex.request import auth_post


def offers_active(key, secret_key, **params):
    """ Get active funding offers.
    Docs: https://bitfinex.readme.io/v2/reference#rest-auth-funding-offers
    """
    endpoint = 'r/funding/offers/' + params.pop('Symbol')
    return auth_post(key, secret_key, 2, endpoint, params=params)

def offers_hist(key, secret_key, **params):
    """ View your latest inactive offers. Limited to last 3 days and 1 request per minute.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offers-hist
    """
    endpoint = 'offers/hist'
    return auth_post(key, secret_key, 2, endpoint, params=params)