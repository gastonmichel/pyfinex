def account_fees(self, **params):
        """ Check the balance.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-account-info
        """
        endpoint = 'account_infos'
        return self.request(endpoint, method='POST', payload_params=params)

def account_infos(self, **params):
    """  See the fees applied to your withdrawals.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-fees
    """
    endpoint = 'account_fees'
    return self.request(endpoint, method='POST', payload_params=params)

def summary(self, **params):
    """  Returns a 30-day summary of your trading volume and return on margin funding.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-summary
    """
    endpoint = 'summary'
    return self.request(endpoint, method='POST', payload_params=params)

def deposit(self, **params):
    """ Return your deposit address to make a new deposit.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-deposit
    """
    endpoint = 'deposit/new'
    return self.request(endpoint, method='POST', payload_params=params)

def key_permissions(self, **params):
    """ Check the permissions of the key being used to generate this request.
    Docs: https://bitfinex.readme.io/v1/reference#auth-key-permissions
    """
    endpoint = 'key_info'
    return self.request(endpoint, method='POST', payload_params=params)

def margin_information(self, **params):
    """ See your trading wallet information for margin trading.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-margin-information
    """
    endpoint = 'margin_infos'
    return self.request(endpoint, method='POST', payload_params=params)

def wallet_balances(self, **params):
    """ See your balances.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-wallet-balances
    """
    endpoint = 'balances'
    return self.request(endpoint, method='POST', payload_params=params)

def tansfer_between_wallets(self, **params):
    """ Allow you to move available balances between your wallets.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-transfer-between-wallets
    """
    endpoint = 'transfer'
    return self.request(endpoint, method='POST', payload_params=params)

def withdrawal(self, **params):
    """ Allow you to request a withdrawal from one of your wallet.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-withdrawal
    """
    endpoint = 'withdraw'
    return self.request(endpoint, method='POST', payload_params=params)