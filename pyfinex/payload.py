from enum import Enum

class payload(object):
    
    def new_order(self, symbol, amount, price, side, type, exchange='bitfinex', is_hidden=False, is_postonly=False):
        payload = {
            'symbol' = symbol,
            'amount': amount,
            'price': price,
            'side': side,
            'type': 'exchange market',
            'exchange': exchange,
            'is_hidden': is_hidden,
            'is_postonly': is_postonly
            }
        return payload

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