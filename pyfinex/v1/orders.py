def new_order(self, **params):
        """ Submit a new order.
        Docs: https://bitfinex.readme.io/v1/reference#rest-auth-orders
        """
        endpoint = 'order/new'
        return self.request(endpoint, method='POST', payload_params=params)

def multiple_new_orders(self, **params): #TODECIDE: enforce params or not
    """ Submit several new orders at once.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-multiple-new-orders
    """
    endpoint = 'order/new/multi'
    return self.request(endpoint, method='POST', payload_params=params)

def cancel_order(self, **params):
    """ Cancel an order.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-order
    """
    endpoint = 'order/cancel'
    return self.request(endpoint, method='POST', payload_params=params)

def cancel_multiple_orders(self, **params):
    """ Cancel multiples orders at once.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-multiple-orders
    """
    endpoint = 'order/cancel/multi'
    return self.request(endpoint, method='POST', payload_params=params)

def cancel_all_orders(self, **params):
    """ Cancel multiples orders at once.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-cancel-all-orders
    """
    endpoint = 'order/cancel/all'
    return self.request(endpoint, method='POST', payload_params=params)

def replace_order(self, **params):
    """ Replace an orders with a new one.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-replace-order
    """
    endpoint = 'order/cancel/replace'
    return self.request(endpoint, method='POST', payload_params=params)

def order_status(self, **params):
    """ Get the status of an order. Is it active? Was it cancelled? To what extent has it been executed? etc.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-order-status
    """
    endpoint = 'order/status'
    return self.request(endpoint, method='POST', payload_params=params)

def active_orders(self, **params):
    """ View your active orders.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-active-orders
    """
    endpoint = 'orders'
    return self.request(endpoint, method='POST', payload_params=params)

def orders_history(self, **params):
    """ View your active orders.
    Docs: https://bitfinex.readme.io/v1/reference#rest-auth-orders-history
    """
    endpoint = 'orders/hist'
    return self.request(endpoint, method='POST', payload_params=params)