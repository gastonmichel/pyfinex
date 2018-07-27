from ..api import request

def offer_new(key, secret_key, **params):
    """ Submit a new offer.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-new-offer
    """
    endpoint = 'offer/new'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def offer_cancel(key, secret_key, **params):
    """ Cancel an offer.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-offer
    """
    endpoint = 'offer/cancel'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def offer_status(key, secret_key, **params):
    """ Get the status of an offer. Is it active? Was it cancelled? To what extent has it been executed? etc.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offer-status
    """
    endpoint = 'offer/status'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def offers_active(key, secret_key, **params):
    """ View your active offers.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offers
    """
    endpoint = 'offers'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def offers_hist(key, secret_key, **params):
    """ View your latest inactive offers. Limited to last 3 days and 1 request per minute.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offers-hist
    """
    endpoint = 'offers/hist'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def active_credits(key, secret_key, **params):
    """ View your funds currently taken (active credits).
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-credits
    """
    endpoint = 'credits'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def active_funding_used_in_a_margin_position(key, secret_key, **params):
    """ View your funding currently borrowed and used in a margin position.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-funding-used-in-a-margin-position
    """
    endpoint = 'taken_funds'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def active_funding_not_used_in_a_margin_position(key, secret_key, **params):
    """ View your funding currently borrowed and not used (available for a new margin position).
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-funding-not-used-in-a-margin-position
    """
    endpoint = 'unused_taken_funds'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def total_taken_funds(key, secret_key, **params):
    """ View the total of your active-funding used in your position(s).
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-total-taken-funds
    """
    endpoint = 'total_taken_funds'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def close_margin_funding(key, secret_key, **params):
    """ Allow you to close an unused or used taken fund
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-close-margin-funding
    """
    endpoint = 'funding/close'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)