def new_offer(self, **params):
        """ Submit a new offer.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-new-offer
        """
        endpoint = 'offer/new'
        return self.request(endpoint, method='POST', payload_params=params)

def cancel_offer(self, **params):
    """ Cancel an offer.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-offer
    """
    endpoint = 'offer/cancel'
    return self.request(endpoint, method='POST', payload_params=params)

def offer_status(self, **params):
    """ Get the status of an offer. Is it active? Was it cancelled? To what extent has it been executed? etc.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offer-status
    """
    endpoint = 'offer/status'
    return self.request(endpoint, method='POST', payload_params=params)

def active_credits(self, **params):
    """ View your funds currently taken (active credits).
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-credits
    """
    endpoint = 'credits'
    return self.request(endpoint, method='POST', payload_params=params)

def offers(self, **params):
    """ View your active offers.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offers
    """
    endpoint = 'offers'
    return self.request(endpoint, method='POST', payload_params=params)

def offers_hist(self, **params):
    """ View your latest inactive offers. Limited to last 3 days and 1 request per minute.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-offers-hist
    """
    endpoint = 'offers/hist'
    return self.request(endpoint, method='POST', payload_params=params)

def mytrades_funding(self, **params):
    """ View your past trades.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-mytrades-funding
    """
    endpoint = 'mytrades_funding'
    return self.request(endpoint, method='POST', payload_params=params)

def active_funding_used_in_a_margin_position(self, **params):
    """ View your funding currently borrowed and used in a margin position.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-funding-used-in-a-margin-position
    """
    endpoint = 'taken_funds'
    return self.request(endpoint, method='POST', payload_params=params)

def active_funding_not_used_in_a_margin_position(self, **params):
    """ View your funding currently borrowed and not used (available for a new margin position).
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-funding-not-used-in-a-margin-position
    """
    endpoint = 'unused_taken_funds'
    return self.request(endpoint, method='POST', payload_params=params)

def total_taken_funds(self, **params):
    """ View the total of your active-funding used in your position(s).
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-total-taken-funds
    """
    endpoint = 'total_taken_funds'
    return self.request(endpoint, method='POST', payload_params=params)

def close_margin_funding(self, **params):
    """ Allow you to close an unused or used taken fund
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-close-margin-funding
    """
    endpoint = 'funding/close'
    return self.request(endpoint, method='POST', payload_params=params)