from enum import Enum


class side(Enum):
    buy = 'buy'
    sell = 'sell'

class margin_order(Enum):
    market = 'market'
    limit = 'limit'
    stop = 'stop'
    trailig_stop = 'trailing-stop'
    fill_or_kill = 'fill_or_kill'

class exchange_order(margin_order):
    exchange_market = 'exchange ' + margin_order.market
    exchange_limit = 'exchange ' + margin_order.limit
    exchange_stop = 'exchange ' + margin_order.stop
    exchange_trailing_stop = 'exchange ' + margin_order.fill_or_kill


class Order:
    def __init__(self, symbol, amount, price, side=side.buy, order_type=margin_order.limit, exchange='bitfinex', is_hidden=False, is_postonly=False):
        self.symbol = symbol
        self.amount = amount
        self.price = price
        self.side = side
        self.type = order_type
        self.exchange = exchange
        self.is_hidden = is_hidden
        self.is_postonly = is_postonly
        

o = Order()

class OCO_order(Order):
    pass
    