def balance_history(self, **params):
        """ View all of your balance ledger entries.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-balance-history
        """
        endpoint = 'history'
        return self.request(endpoint, method='POST', payload_params=params)

def deposit_withdrawal_history(self, **params):
    """ View all of your balance ledger entries.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-deposit-withdrawal-history
    """
    endpoint = 'history/movements'
    return self.request(endpoint, method='POST', payload_params=params)

def past_trades(self, **params):
    """ View all of your balance ledger entries.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-past-trades
    """
    endpoint = 'mytrades'
    return self.request(endpoint, method='POST', payload_params=params)