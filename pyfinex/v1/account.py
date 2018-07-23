from pyfinex.request import auth_post

def info(key, secret_key, **params):
    """ Check the balance.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-account-info
    """
    endpoint = 'account_infos'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def withdrawals_fees(key, secret_key, **params):
    """  See the fees applied to your withdrawals.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-fees
    """
    endpoint = 'account_fees'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def summary(key, secret_key, **params):
    """  Returns a 30-day summary of your trading volume and return on margin funding.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-summary
    """
    endpoint = 'summary'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def deposit_adress(key, secret_key, **params):
    """ Return your deposit address to make a new deposit.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-deposit
    """
    endpoint = 'deposit/new'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def key_permissions(key, secret_key, **params):
    """ Check the permissions of the key being used to generate this request.
    Docs: https://bitfinex.readme.io/v1/reference#auth-key-permissions
    """
    endpoint = 'key_info'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def margin_info(key, secret_key, **params):
    """ See your trading wallet information for margin trading.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-margin-information
    """
    endpoint = 'margin_infos'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def wallet_balances(key, secret_key, **params):
    """ See your balances.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-wallet-balances
    """
    endpoint = 'balances'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def tansfer_between_wallets(key, secret_key, **params):
    """ Allow you to move available balances between your wallets.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-transfer-between-wallets
    """
    endpoint = 'transfer'
    return auth_post(key, secret_key, 1, endpoint, params=params)

def withdraw(key, secret_key, **params):
    """ Allow you to request a withdrawal from one of your wallet.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-withdrawal
    """
    endpoint = 'withdraw'
    return auth_post(key, secret_key, 1, endpoint, params=params)