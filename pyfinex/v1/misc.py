
def basket_manage(self, **params):
    """ This endpoint is used to manage the creation or destruction of tokens via splitting or merging. For the moment, this is only useful for the bcc and bcu tokens.
    Docs: https://bitfinex.readme.io/v1/reference#basket-manage
    """
    endpoint = 'basket_manage'
    return self.request(endpoint, method='POST', payload_params=params)