from ..api import request

def active(key, secret_key, **params):
    """ View your active positions.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-positions
    """
    endpoint = 'positions'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def claim(key, secret_key, **params):
    """ A position can be claimed if:
    It is a long position:
        The amount in the last unit of the position pair that you have in your trading wallet AND/OR the realized profit of the position is greater or equal to the purchase amount of the position (base price * position amount) and the funds which need to be returned.
        For example, for a long BTCUSD position, you can claim the position if the amount of USD you have in the trading wallet is greater than the base price * the position amount and the funds used.
    It is a short position:
        The amount in the first unit of the position pair that you have in your trading wallet is greater or equal to the amount of the position and the margin funding used.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-claim-position
    """
    endpoint = 'position/claim'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)

def close(key, secret_key, **params):
    """ Closes the selected position with a market order.
    Docs: https://bitfinex.readme.io/v1/reference#close-position
    """
    endpoint = 'position/close'
    return request(authenticate=True, key=key, secret_key=secret_key, version=1, endpoint=endpoint, method='POST', body_params=params)