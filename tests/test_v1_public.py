# from pyfinex import v1
import pytest

import pyfinex

def test_ticker():
    resp = pyfinex.v1.public.ticker(symbol='btcusd')
    resp['mid']

def test_stats():
    resp = pyfinex.v1.public.stats(symbol='btcusd')
    resp[0]['period']

def test_lendbook():
    resp = pyfinex.v1.public.funding_book(currency = 'usd')
    resp['bids'][0]['rate']

def test_orderbook():
    resp = pyfinex.v1.public.order_book(symbol='btcusd')
    resp['bids'][0]['price']
    